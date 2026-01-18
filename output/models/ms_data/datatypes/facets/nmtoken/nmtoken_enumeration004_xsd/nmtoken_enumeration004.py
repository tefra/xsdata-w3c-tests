from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class FooAttrTest(Enum):
    FOO = "foo"
    FOO123 = "foo123"
    FU1 = "fu1"


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
        attr_test: None | FooAttrTest = field(
            default=None,
            metadata={
                "name": "attrTest",
                "type": "Attribute",
            },
        )


@dataclass(kw_only=True)
class Test(FooType):
    class Meta:
        name = "test"
