from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(kw_only=True)
class MyType:
    class Meta:
        name = "myType"

    my_element1: None | str = field(
        default=None,
        metadata={
            "name": "myElement1",
            "type": "Element",
            "namespace": "",
        },
    )
    my_element2: None | str = field(
        default=None,
        metadata={
            "name": "myElement2",
            "type": "Element",
            "namespace": "",
        },
    )
    my_element3: None | str = field(
        default=None,
        metadata={
            "name": "myElement3",
            "type": "Element",
            "namespace": "",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class FooType(MyType):
    class Meta:
        name = "fooType"

    my_element2: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    my_element3: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    any_attributes: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    my_element1: str = field(
        metadata={
            "name": "myElement1",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    my_attr: None | object = field(
        default=None,
        metadata={
            "name": "myAttr",
            "type": "Attribute",
        },
    )
    my_attr2: None | object = field(
        default=None,
        metadata={
            "name": "myAttr2",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Root(FooType):
    class Meta:
        name = "root"
