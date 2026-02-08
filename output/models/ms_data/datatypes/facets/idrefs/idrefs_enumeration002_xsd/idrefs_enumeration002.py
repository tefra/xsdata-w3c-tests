from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class FooIdrefsAttr(Enum):
    FOO = "foo"


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"

    idrefs_attr: None | FooIdrefsAttr = field(
        default=None,
        metadata={
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
class FooType:
    class Meta:
        name = "fooType"

    foo: Foo = field(
        metadata={
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class Test(FooType):
    class Meta:
        name = "test"
