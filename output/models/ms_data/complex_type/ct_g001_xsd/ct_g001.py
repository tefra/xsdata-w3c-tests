from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(kw_only=True)
class MyType:
    class Meta:
        name = "myType"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    my_attr: None | object = field(
        default=None,
        metadata={
            "name": "myAttr",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class FooType(MyType):
    class Meta:
        name = "fooType"

    any_element: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    my_element: str = field(
        metadata={
            "name": "myElement",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Root(FooType):
    class Meta:
        name = "root"
