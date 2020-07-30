import json
import textwrap
from collections import defaultdict
from dataclasses import asdict
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Dict
from typing import Iterator
from typing import List
from typing import Union

from lxml import etree
from xsdata.formats.dataclass.filters import class_name
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.utils import text

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
def test_{name}(save_xml):
{documentation}
    assert_bindings(
        schema="{schema_path}",
        instance="{instance_path}",
        class_name="{class_name}",
        version="{version}",
        save_xml=save_xml,
    )
"""

test_ns_struct_case_tpl = """{decorators}
def test_{name}(save_xml):
{documentation}
    assert_bindings(
        schema="{schema_path}",
        instance="{instance_path}",
        class_name="{class_name}",
        version="{version}",
        ns_struct=True,
        save_xml=save_xml,
    )
"""


xfails = dict()
lastfailed = root.joinpath(".pytest_cache/v/cache/lastfailed")
if lastfailed.exists():
    with lastfailed.open() as f:
        xfails = json.load(f)


@dataclass
class TestCase:
    path: Path
    version: str
    documentation: str
    schema_name: str
    schema_path: Union[Path, str]
    schema_is_valid: bool
    instance_name: str
    instance_path: Path
    instance_is_valid: bool
    class_name: str
    ns_struct: bool


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
        output = render_test_cases(test_file.relative_to(root), chunk_cases)

        if output.find("pytest.mark") == -1:
            output = "\n".join(output.split("\n")[2:])

        print(f"Generating: {test_file.relative_to(root)}")
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
        if case.version == "1.1":
            markers.append("@pytest.mark.schema11")
        if xfails.get(f"{test_file}::test_{name}"):
            markers.append("@pytest.mark.xfail")
        if not case.schema_path:
            markers.append('@pytest.mark.skip(reason="No schema")')
        elif not case.schema_is_valid:
            markers.append('@pytest.mark.skip(reason="Invalid schema")')
        elif not case.instance_is_valid:
            markers.append('@pytest.mark.skip(reason="Invalid instance")')

        if markers:
            markers.insert(0, "")

        decorators = "\n".join(markers)
        template = test_ns_struct_case_tpl if case.ns_struct else test_case_tpl
        output.append(template.format(name=name, decorators=decorators, **asdict(case)))

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
    ns_struct = False

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

    if group.name in ("schD5", "schD7",):
        ns_struct = True

    for instance in group.instance_test:
        if not instance.instance_document or not instance.instance_document.href:
            raise ValueError("Missing instance document!")

        instance_path = path.joinpath(instance.instance_document.href).resolve()
        instance_href = instance_path.relative_to(w3c)
        instance_validity = validity(instance.expected)
        class_name = read_root_name(instance_path)
        version = pick_version(group.version)

        yield TestCase(
            path=path,
            version=version,
            documentation=documentation,
            schema_name=schema_name,
            schema_path=schema_href or "",
            schema_is_valid=schema_is_valid,
            instance_name=text.snake_case(instance.name),
            instance_path=instance_href,
            instance_is_valid=instance_validity.validity == ExpectedOutcome.VALID,
            class_name=class_name,
            ns_struct=ns_struct,
        )


def read_root_name(path: Path) -> str:
    try:
        recovering_parser = etree.XMLParser(recover=True)
        tree = etree.parse(str(path), parser=recovering_parser)
        root = tree.getroot()
        return class_name(etree.QName(root.tag).localname)
    except etree.XMLSyntaxError:
        return ""
    except OSError:
        return ""


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
    documentation = "\n".join(
        textwrap.wrap(
            "\n".join(
                [
                    element.text or "" if isinstance(element, AnyElement) else element
                    for annotation in group.annotation
                    for documentation in annotation.documentation
                    for element in documentation.any_element
                    if element
                ]
            )
        )
    )

    if documentation:
        raw = "r" if documentation.find("\\") > -1 else ""
        return textwrap.indent(f'{raw}"""\n{documentation}\n"""', "    ")

    return ""


if __name__ == "__main__":
    generate()
