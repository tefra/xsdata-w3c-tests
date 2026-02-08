from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class FooAttrTest(Enum):
    FOO = "foo"


@dataclass(kw_only=True)
class FooType:
    class Meta:
        name = "fooType"

    foo: FooType.Foo = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )

    @dataclass(kw_only=True)
    class Foo:
        value: str = field(default="")
        attr_test: None | FooAttrTest = field(
            default=None,
            metadata={
                "name": "attrTest",
                "type": "Attribute",
            },
        )
        id_attr: None | str = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass(kw_only=True)
class Test(FooType):
    class Meta:
        name = "test"
