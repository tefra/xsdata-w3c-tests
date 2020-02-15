import io
import json
import textwrap
from collections import defaultdict
from dataclasses import asdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict
from typing import Iterator
from typing import List
from typing import Union

import yaml
from lxml import etree
from xsdata.formats.dataclass.models import AnyElement
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.generators import PythonAbstractGenerator
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

test_case_tpl = """{marker}
def test_{name}():
{documentation}
    assert_bindings(
        schema="{schema_path}",
        is_valid={schema_is_valid},
        instance="{instance_path}",
        instance_is_valid={instance_is_valid},
        class_name="{class_name}",
        version="{version}",
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


def generate():
    test_cases: Dict[str, List[TestCase]] = defaultdict(list)
    for test_case in fetch_test_cases():
        test_cases[test_case.path.stem].append(test_case)

    for test_file in tests.glob("test_*.py"):
        test_file.unlink()

    test_files = []
    for group, cases in test_cases.items():
        num = 0
        for chunk_cases in chunks(cases, 1000):
            num += len(chunk_cases)
            test_file = tests.joinpath(f"test_{text.snake_case(group)}_{num}.py")
            output = render_test_cases(test_file.relative_to(root), chunk_cases)

            if output.find("pytest.mark") == -1:
                output = "\n".join(output.split("\n")[2:])

            test_file.write_text(output)
            test_files.append(str(test_file.relative_to(w3c.parent)))

    travis = root.joinpath(".travis.yml")
    config = yaml.full_load(travis.read_text())
    config["env"] = [f"TESTFILE={test_file}" for test_file in test_files]
    travis.write_text(
        yaml.dump(config, sort_keys=False, default_flow_style=False, indent=4)
    )


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def render_test_cases(test_file, cases: List[TestCase]) -> str:
    output = []
    names: Dict[str, int] = defaultdict(int)
    for case in cases:
        name = f"{case.schema_name}_{case.instance_name}"
        if name in names:
            name = f"{name}_{len(names)}"
        names[name] += 1

        marker = ""
        if xfails.get(f"{test_file}::test_{name}"):
            marker = "\n@pytest.mark.xfail"

        output.append(test_case_tpl.format(name=name, marker=marker, **asdict(case)))

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
    version = "1.0"

    if (
        group.schema_test
        and group.schema_test.schema_document
        and group.schema_test.schema_document[0].href
    ):
        schema_href = (
            path.joinpath(group.schema_test.schema_document[0].href)
            .resolve()
            .relative_to(w3c)
        )
        schema_validity = validity(group.schema_test.expected)
        version = schema_validity.version or "1.0"
        schema_is_valid = schema_validity.validity == ExpectedOutcome.VALID

    version = group.version or version
    schema_name = text.snake_case(group.name)
    documentation = make_docstring(group)

    for instance in group.instance_test:
        if not instance.instance_document or not instance.instance_document.href:
            raise ValueError("Missing instance document!")

        instance_path = path.joinpath(instance.instance_document.href).resolve()
        instance_href = instance_path.relative_to(w3c)
        instance_validity = validity(instance.expected)
        class_name = read_root_name(instance_path)

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
        )


def read_root_name(path: Path) -> str:
    try:
        document = path.read_bytes()
        tree = etree.parse(io.BytesIO(document))
        root = tree.getroot()
        return PythonAbstractGenerator.class_name(etree.QName(root.tag).localname)
    except etree.XMLSyntaxError:
        return ""
    except FileNotFoundError:
        return ""


def validity(expects: List[Expected]) -> Expected:
    expect = None
    if len(expects) > 1:
        expect = next(
            (exp for exp in expects if exp.validity == ExpectedOutcome.VALID), None
        )

    return expect if expect else expects[0]


def make_docstring(group: TestGroup) -> str:
    documentation = "\n".join(
        textwrap.wrap(
            "\n".join(
                [
                    element.text or "" if isinstance(element, AnyElement) else element
                    for annotation in group.annotation
                    for documentation in annotation.documentation
                    for element in documentation.elements
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
