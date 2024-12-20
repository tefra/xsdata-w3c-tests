import json
import textwrap
from collections import defaultdict
from enum import Enum
from pathlib import Path
from typing import Dict
from typing import Iterator
from typing import List
from typing import NamedTuple

from lxml import etree
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.utils import text
from xsdata.utils.namespaces import local_name

from models.xsts import Expected
from models.xsts import ExpectedOutcome
from models.xsts import TestGroup
from models.xsts import TestSet
from models.xsts import TestSuite

root = Path(__file__).absolute().parent
w3c = root.joinpath("w3c")
tests = root.joinpath("tests")

test_module_tpl = """import pytest

from tests.utils import assert_bindings\n\n{}"""

test_case_tpl = """{decorators}
def test_{name}(mode, save_output, output_format):
{test.documentation}
    assert_bindings(
        schema="{test.schema_path}",
        instance="{test.instance_path}",
        class_name="{test.class_name}",
        version="{test.version}",
        mode=mode,
        save_output=save_output,
        output_format=output_format,
        structure_style="{test.structure_style}",
    )
"""


xfails = dict()
lastfailed = root.joinpath(".pytest_cache/v/cache/lastfailed")
if lastfailed.exists():
    with lastfailed.open() as f:
        xfails = json.load(f)


class TestCase(NamedTuple):
    path: Path
    version: str
    documentation: str
    schema_name: str
    schema_path: str
    instance_name: str
    instance_path: str
    class_name: str
    structure_style: str


def generate():
    for test_file in tests.glob("test_*.py"):
        if test_file.stem != "test_performance":
            test_file.unlink()

    prev = None
    test_cases = []
    for test_case in fetch_test_cases():
        group = test_case.path.stem
        if prev and prev != group:
            write_test_file(prev, test_cases)
            test_cases.clear()

        test_cases.append(test_case)
        prev = group

    if prev and test_cases:
        write_test_file(group, test_cases)


def write_test_file(group: str, cases: List[TestCase]):
    num = 0
    for chunk_cases in chunks(cases, 1000):
        num += len(chunk_cases)
        test_file = tests.joinpath(f"test_{text.snake_case(group)}_{num}.py")
        test_file_relative = test_file.relative_to(root)
        output = render_test_cases(test_file_relative, chunk_cases)

        if output.find("pytest.mark") == -1:
            output = "\n".join(output.split("\n")[2:])

        print(f"Generating: {test_file_relative}")
        test_file.write_text(output)


def chunks(lst, n):
    for i in range(0, len(lst), n):
        end = i + n
        yield lst[i:end]


def render_test_cases(test_file, cases: List[TestCase]) -> str:
    output = []
    names: Dict[str, int] = defaultdict(int)
    for case in cases:
        name = f"{case.schema_name}_{case.instance_name}"
        if name in names:
            name = f"{name}_{len(names)}"
        names[name] += 1

        markers = []

        if xfails.get(f"{test_file}::test_{name}"):
            markers.append("@pytest.mark.xfail")

        if markers:
            markers.insert(0, "")

        decorators = "\n".join(markers)
        output.append(test_case_tpl.format(name=name, decorators=decorators, test=case))

    return test_module_tpl.format("\n".join(output))


def fetch_test_cases() -> Iterator[TestCase]:
    suite = XmlParser().from_path(w3c.joinpath("suite.xml"), TestSuite)
    parser = XmlParser()

    for test_set_ref in suite.test_set_ref:
        test_set_ref_path = w3c.joinpath(test_set_ref.href)
        path = test_set_ref_path.parent

        test_set = parser.from_path(test_set_ref_path, TestSet)
        for test_group in reversed(test_set.test_group):
            for test_case in make_test_cases(path, test_group):
                yield test_case


def make_test_cases(path: Path, group: TestGroup):
    schema_href = None
    schema_is_valid = False

    if (
        group.schema_test
        and group.schema_test.schema_document
        and group.schema_test.schema_document[0].href
    ):
        schema_doc = group.schema_test.schema_document[0].href
        schema_validity = validity(group.schema_test.expected)
        if (
            group.name in ("wildZ003", "ctZ007")
            and len(group.schema_test.schema_document) > 0
            and group.schema_test.schema_document[1].href
        ):
            schema_doc = group.schema_test.schema_document[1].href

        schema_href = path.joinpath(schema_doc).resolve().relative_to(w3c)

        schema_is_valid = schema_validity.validity == ExpectedOutcome.VALID

    schema_name = text.snake_case(group.name)
    documentation = make_docstring(group)

    structure_style = "filenames"
    if group.name in ("schD5", "schD7", "xsd003b", "over015"):
        structure_style = "namespaces"
    elif group.name in ("addB132", "ctZ007"):
        structure_style = "single-package"

    for instance in group.instance_test:
        if not instance.instance_document or not instance.instance_document.href:
            raise ValueError("Missing instance document!")

        instance_path = path.joinpath(instance.instance_document.href).resolve()
        instance_href = instance_path.relative_to(w3c)
        instance_validity = validity(instance.expected)
        class_name = read_root_name(instance_path)
        version = pick_version(group.version)
        instance_is_valid = instance_validity.validity == ExpectedOutcome.VALID
        schema_path = str(schema_href) or ""
        if schema_path and instance_is_valid and schema_is_valid:
            yield TestCase(
                path=path,
                version=version,
                documentation=documentation,
                schema_name=schema_name,
                schema_path=schema_path,
                instance_name=text.snake_case(instance.name),
                instance_path=str(instance_href),
                class_name=class_name,
                structure_style=structure_style,
            )


def validity(expects: List[Expected]) -> Expected:
    expect = None
    if len(expects) > 1:
        expect = next(
            (exp for exp in expects if exp.validity == ExpectedOutcome.VALID), None
        )

    return expect if expect else expects[0]


def pick_version(versions: List):
    choices = set(v.value if isinstance(v, Enum) else str(v) for v in versions)
    if "1.1" in choices:
        return "1.1"
    elif "1.0" in choices:
        return "1.0"
    else:
        return "1.1"


def make_docstring(group: TestGroup) -> str:
    raw = "\n".join(
        element.text or "" if isinstance(element, AnyElement) else str(element)
        for annotation in group.annotation
        for documentation in annotation.documentation
        for element in documentation.content
        if element
    )

    documentation = "\n".join(textwrap.wrap(" ".join(raw.split())))
    if documentation:
        raw = "r" if documentation.find("\\") > -1 else ""
        return textwrap.indent(f'{raw}"""\n{documentation}\n"""', "    ")

    return ""


def read_root_name(path: Path) -> str:
    try:
        recovering_parser = etree.XMLParser(
            recover=True, resolve_entities=False, no_network=True
        )
        tree = etree.parse(str(path), parser=recovering_parser)  # nosec
        name = text.pascal_case(local_name(tree.getroot().tag))

        if text.is_reserved(name):
            return text.pascal_case(f"{name}_Type")

        return name
    except Exception:
        return ""


if __name__ == "__main__":
    generate()
