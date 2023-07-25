import functools
import logging
import os
from pathlib import Path

import pytest
import xmlschema
from click.testing import CliRunner
from lxml import etree
from typing import Any
from typing import Dict
from typing import Optional
from xsdata.cli import cli
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import PycodeSerializer
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.utils import text
from xsdata.utils.testing import load_class

log = logging.getLogger()

root = Path(__file__).absolute().parent.parent
w3c = root.joinpath("w3c")
output = root.joinpath("output/instances")
os.chdir(w3c.parent)
config = SerializerConfig(pretty_print=True)


def assert_bindings(
    schema: str,
    instance: str,
    class_name: str,
    version: str,
    mode: str,
    save_output: bool,
    output_format: str,
    structure_style: str,
):
    __tracebackhide__ = True

    schema_path = Path(schema)
    pck_arr = list(map(text.snake_case, schema_path.parts))
    package = f"output.models.{'.'.join(pck_arr)}"
    schema_path = w3c.joinpath(schema)
    source = str(schema_path)

    clazz = generate_models(source, package, class_name, output_format, structure_style)

    if mode == "build":
        return

    if isinstance(clazz, Exception):
        raise clazz

    models_package = None
    if clazz is not None:
        levels = package.count(".")
        models_package = ".".join(clazz.__module__.split(".")[: levels + 1])

    try:
        instance_path = w3c.joinpath(instance)
        schema_path = w3c.joinpath(schema)
        context = XmlContext(class_type=output_format, models_package=models_package)
        parser = XmlParser(context=context)
        obj = parser.from_path(instance_path, clazz)
    except Exception as e:
        raise e

    save_path = None
    if save_output:
        save_path = output.joinpath(instance)
        save_path.parent.mkdir(parents=True, exist_ok=True)

    assert_xml_bindings(
        context,
        obj,
        parser.ns_map,
        schema_path,
        instance_path,
        save_path,
        version,
    )


def assert_xml_bindings(
    context: XmlContext,
    obj: Any,
    ns_map: Dict,
    schema_path: Path,
    instance_path: Path,
    save_path: Optional[Path],
    version: str,
):
    __tracebackhide__ = True

    schema_validator = get_validator(schema_path, version)
    if schema_validator is None:
        pytest.skip("Schema validator failed on parsing definition")

    try:
        xsdata_xml = XmlSerializer(context=context, config=config).render(obj, ns_map)
        if save_path:
            save_path.write_text(xsdata_xml)
            code = PycodeSerializer(context=context, config=config).render(obj)
            save_path.with_suffix(".py").write_text(code)

        return assert_valid(schema_validator, xsdata_xml)
    except Exception as e:
        try:
            original_tree = etree.parse(str(instance_path))
            assert_valid(schema_validator, original_tree)
        except Exception:
            pytest.skip("Original instance failed to validate!")

        raise e


def assert_valid(validator, tree):
    __tracebackhide__ = True
    validator.validate(tree)


@functools.lru_cache(maxsize=5)
def generate_models(
    xsd: str, package: str, class_name: str, output_format: str, structure_style: str
):
    runner = CliRunner()
    result = runner.invoke(
        cli,
        [
            xsd,
            "-ss",
            structure_style,
            "-p",
            package,
            "-o",
            output_format,
            "--compound-fields",
        ],
    )

    if result.exception:
        return result.exception

    try:
        return load_class(result.output, class_name)
    except ModuleNotFoundError:
        return None


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
