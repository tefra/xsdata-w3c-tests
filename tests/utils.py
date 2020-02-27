import functools
import importlib
import logging
import os
from pathlib import Path

import pytest
import xmlschema
from click.testing import CliRunner
from xsdata import cli
from xsdata.formats.dataclass.generator import DataclassGenerator
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.reducer import reducer
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

    reducer.common_types.clear()
    writer.register_generator("pydata", DataclassGenerator())
    writer.get_renderer("pydata").modules.clear()

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
        else:
            return

    schema_validator = get_validator(schema_path_absolute, version, is_valid)
    if schema_validator:
        try:
            schema_validator.validate(XmlSerializer().render(obj))
        except Exception as e:
            if instance_is_valid:
                raise e


@functools.lru_cache(maxsize=5)
def generate_models(xsd: str, package: str):
    runner = CliRunner()
    return runner.invoke(cli, [xsd, f"--package={package}"])


@functools.lru_cache(maxsize=5)
def get_validator(path: Path, version: str, is_valid: bool):
    try:
        schema_class = (
            xmlschema.XMLSchema11 if version == "1.1" else xmlschema.XMLSchema10
        )
        return schema_class(str(path))
    except Exception as e:
        if is_valid:
            pytest.skip("Schema validator failed on parsing definition")


def load_class(output, clazz_name):
    search = "Generating package: "
    packages = [
        line[len(search) :] for line in output.split("\n") if line.startswith(search)
    ]

    for package in reversed(packages):
        try:
            module = importlib.import_module(package)
            return getattr(module, clazz_name)
        except (ModuleNotFoundError, AttributeError):
            pass

    pytest.fail(f"Failed to load class name {clazz_name}")
