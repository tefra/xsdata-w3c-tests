import contextlib
import difflib
import functools
import logging
import os
from pathlib import Path
from typing import Any
from typing import Dict
from typing import Optional

import pytest
import xmlschema
from click.testing import CliRunner
from lxml import etree
from xsdata.cli import cli
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import JsonParser
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import JsonSerializer
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.utils import text
from xsdata.utils.testing import load_class

log = logging.getLogger()

w3c = Path(__file__).absolute().parent.parent.joinpath("w3c")
output = Path(__file__).absolute().parent.parent.joinpath("output/instances")
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

    if mode == "xml":
        instance_path = Path(instance)
        pck_arr = list(map(text.snake_case, instance_path.parts))
        package = f"output.xml_models.{'.'.join(pck_arr)}"
        instance_path = w3c.joinpath(instance_path)
        source = str(instance_path)
    else:
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

    try:
        instance_path = w3c.joinpath(instance)
        schema_path = w3c.joinpath(schema)
        context = XmlContext(class_type=output_format)
        parser = XmlParser(context=context)
        obj = parser.from_path(instance_path, clazz)
    except Exception as e:
        raise e

    save_path = None
    if save_output:
        save_path = output.joinpath(instance)
        save_path.parent.mkdir(parents=True, exist_ok=True)

    if mode == "json":
        assert_json_bindings(context, obj, save_path)
    else:
        assert_xml_bindings(
            context, obj, parser.ns_map, schema_path, instance_path, save_path, version
        )


def assert_json_bindings(context: XmlContext, obj: Any, save_path: Optional[Path]):
    __tracebackhide__ = True

    serializer = JsonSerializer(context=context, config=config)
    parser = JsonParser(context=context)
    obj_json = serializer.render(obj)
    obj_b = parser.from_string(obj_json, obj.__class__)

    if save_path:
        save_path.with_suffix(".json").write_text(obj_json)

        with contextlib.suppress(FileNotFoundError):
            save_path.with_suffix(".diff").unlink()

    if obj != obj_b:
        obj_b_json = serializer.render(obj_b)

        if obj_json == obj_b_json:
            return

        diff = "\n".join(difflib.ndiff(obj_json.splitlines(), obj_b_json.splitlines()))

        if save_path:
            save_path.with_suffix(".diff").write_text(diff)

        raise AssertionError(f"JSON Round trip failed\n{diff}")


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
            json_document = JsonSerializer(context=context, config=config).render(obj)
            save_path.write_text(xsdata_xml)
            save_path.with_suffix(".json").write_text(json_document)
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
        cli, [xsd, "-ss", structure_style, "-p", package, "-o", output_format, "-cf"]
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
