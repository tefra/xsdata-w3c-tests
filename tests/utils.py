import functools
import importlib
import logging
import os
from pathlib import Path

import pytest
import xmlschema
from click.testing import CliRunner
from lxml import etree
from xsdata import cli
from xsdata.analyzer import analyzer
from xsdata.formats.dataclass.generator import DataclassGenerator
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.utils import text
from xsdata.writer import writer

log = logging.getLogger()

w3c = Path(__file__).absolute().parent.parent.joinpath("w3c")
os.chdir(w3c.parent)


def assert_bindings(
    schema: str,
    is_valid: bool,
    instance: str,
    instance_is_valid: bool,
    class_name: str,
    version: str,
):
    __tracebackhide__ = True
    if not schema:
        pytest.skip("No schema for code generator")
    if not is_valid:
        pytest.skip("Invalid schema")

    analyzer.common_types.clear()
    writer.register_format("pydata", DataclassGenerator())

    schema_path = Path(schema)
    schema_path_absolute = w3c.joinpath(schema)

    package = f"tests.output.{'.'.join(map(text.snake_case, schema_path.parent.parts))}"
    result = generate_models(str(w3c.joinpath(schema)), package)

    if is_valid and result.exception:
        raise result.exception

    if not class_name:
        pytest.skip("No class name for data binding")

    clazz = load_class(result.output, class_name)
    parser = XmlParser()

    try:
        obj = parser.from_path(w3c.joinpath(instance), clazz)
    except Exception as e:
        if instance_is_valid:
            raise e

    if not instance_is_valid:
        return

    schema_validator = get_validator(schema_path_absolute, version)
    if schema_validator is None and is_valid:
        pytest.skip("Schema validator failed on parsing definition")

    tree = None
    try:
        tree = XmlSerializer().render_tree(obj)
        return assert_valid(schema_validator, tree)
    except Exception as e:
        try:
            original_tree = etree.parse(str(w3c.joinpath(instance)))
            assert_valid(schema_validator, original_tree)
        except Exception as f:
            pytest.skip("Original instance failed to validate!")

        if tree is not None:
            xml_instance = etree.tostring(tree, pretty_print=True).decode()
            log.error(xml_instance)

        raise e


def assert_valid(validator, tree):
    __tracebackhide__ = True
    if isinstance(validator, xmlschema.XMLSchema11):
        validator.validate(tree)
    else:
        validator.assertValid(tree)


@functools.lru_cache(maxsize=5)
def generate_models(xsd: str, package: str):
    runner = CliRunner()
    return runner.invoke(cli, [xsd, f"--package={package}"])


@functools.lru_cache(maxsize=5)
def get_validator(path: Path, version: str):
    return initialize_validator(path, version)


def initialize_validator(path: Path, version: str):
    try:
        __tracebackhide__ = True
        if version == "1.1":
            return xmlschema.XMLSchema11(str(path))
        else:
            xmlschema_doc = etree.parse(str(path))
            return etree.XMLSchema(xmlschema_doc)
    except Exception:
        if version == "1.1":
            return None
        return initialize_validator(path, "1.1")


def load_class(output, clazz_name):
    search = "Generating package: "
    start = len(search)
    packages = [line[start:] for line in output.split("\n") if line.startswith(search)]

    for package in reversed(packages):
        try:
            module = importlib.import_module(package)
            return getattr(module, clazz_name)
        except (ModuleNotFoundError, AttributeError):
            pass

    pytest.fail(f"Failed to load class name {clazz_name}")
