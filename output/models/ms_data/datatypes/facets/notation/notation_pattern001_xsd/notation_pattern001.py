from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from xml.etree.ElementTree import QName


class BuildNotation(Enum):
    JPEG = QName("jpeg")
    MPEG = QName("mpeg")
    G = QName("g")


@dataclass(kw_only=True)
class FooType:
    class Meta:
        name = "fooType"

    foo: FooType.Foo = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )

    @dataclass(kw_only=True)
    class Foo:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        attr_test: None | BuildNotation = field(
            default=None,
            metadata={
                "name": "attrTest",
                "type": "Attribute",
                "pattern": r"[a-z]{1}peg",
            },
        )


@dataclass(kw_only=True)
class Test(FooType):
    class Meta:
        name = "test"
