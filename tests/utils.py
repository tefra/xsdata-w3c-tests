import contextlib
import difflib
import functools
import logging
import os
import pprint
from dataclasses import asdict
from pathlib import Path
from typing import Any
from typing import Dict
from typing import Optional

import pytest
import xmlschema
from click.testing import CliRunner
from lxml import etree
from xsdata.cli import cli
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
    json_360: bool,
    save_output: bool,
    ns_struct: bool = False,
):
    __tracebackhide__ = True

    schema_path = Path(schema)
    pck_arr = list(map(text.snake_case, schema_path.parts))
    package = f"output.models.{'.'.join(pck_arr)}"
    schema_path = w3c.joinpath(schema)
    clazz = generate_models(str(schema_path), package, class_name, ns_struct)

    if isinstance(clazz, Exception):
        raise clazz

    try:
        instance_path = w3c.joinpath(instance)
        parser = XmlParser()
        obj = parser.from_path(instance_path, clazz)
    except Exception as e:
        raise e

    save_path = None
    if save_output:
        save_path = output.joinpath(instance)
        save_path.parent.mkdir(parents=True, exist_ok=True)

    if json_360:
        assert_json_bindings(obj, save_path)
    else:
        assert_xml_bindings(
            obj, parser.ns_map, schema_path, instance_path, save_path, version
        )


def assert_json_bindings(obj: Any, save_path: Optional[Path]):
    __tracebackhide__ = True

    serializer = JsonSerializer(indent=4)
    parser = JsonParser()
    obj_json = serializer.render(obj)
    obj_b = parser.from_string(obj_json, obj.__class__)

    if save_path:
        save_path.with_suffix(".json").write_text(obj_json)

        with contextlib.suppress(FileNotFoundError):
            save_path.with_suffix(".round.json").unlink()

    if obj != obj_b:
        if save_path:
            save_path.with_suffix(".round.json").write_text(serializer.render(obj_b))

        message = "JSON Round trip failed\n" + "\n".join(
            difflib.ndiff(
                pprint.pformat(asdict(obj)).splitlines(),
                pprint.pformat(asdict(obj_b)).splitlines(),
            )
        )

        raise AssertionError(message)


def assert_xml_bindings(
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
        xsdata_xml = XmlSerializer(config=config).render(obj, ns_map)
        if save_path:
            json_document = JsonSerializer(indent=4).render(obj)
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
def generate_models(xsd: str, package: str, class_name: str, ns_struct: bool):
    runner = CliRunner()
    args = [xsd, "--package", package, "--compound-fields", "true"]
    if ns_struct:
        args.append("--ns-struct")

    result = runner.invoke(cli, args)

    if result.exception:
        return result.exception

    return load_class(result.output, class_name)


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
