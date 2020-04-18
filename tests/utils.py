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
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.utils import text

log = logging.getLogger()

w3c = Path(__file__).absolute().parent.parent.joinpath("w3c")
output = Path(__file__).absolute().parent.parent.joinpath("xsdata")
os.chdir(w3c.parent)


def assert_bindings(
    schema: str, instance: str, class_name: str, version: str, save_xml: bool,
):
    __tracebackhide__ = True

    schema_path = Path(schema)
    schema_path_absolute = w3c.joinpath(schema)

    pck_arr = list(map(text.snake_case, schema_path.parts))
    package = f"tests.output.{'.'.join(pck_arr)}"
    result = generate_models(str(w3c.joinpath(schema)), package)

    if result.exception:
        raise result.exception

    try:
        instance_path = w3c.joinpath(instance)
        clazz = load_class(result.output, class_name)
        parser = XmlParser()
        namespaces = parser.namespaces
        obj = parser.from_path(instance_path, clazz)
    except Exception as e:
        raise e

    schema_validator = get_validator(schema_path_absolute, version)
    if schema_validator is None:
        pytest.skip("Schema validator failed on parsing definition")

    try:
        tree = XmlSerializer().render_tree(obj, parser.namespaces)
        namespaces.unregister()
        if save_xml:
            xsdata_instance = output.joinpath(instance)
            xsdata_instance.parent.mkdir(parents=True, exist_ok=True)
            xsdata_instance.write_bytes(
                b"<!-- xsdata instance -->\n" + etree.tostring(tree, pretty_print=True)
            )
        return assert_valid(schema_validator, tree)
    except Exception as e:
        try:
            original_tree = etree.parse(str(w3c.joinpath(instance)))
            assert_valid(schema_validator, original_tree)
        except Exception:
            pytest.skip("Original instance failed to validate!")

        raise e


def assert_valid(validator, tree):
    __tracebackhide__ = True
    validator.validate(tree)


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
            return xmlschema.XMLSchema10(str(path))
    except Exception:
        return None


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

    raise ModuleNotFoundError(f"Class `{clazz_name}` not found.")
