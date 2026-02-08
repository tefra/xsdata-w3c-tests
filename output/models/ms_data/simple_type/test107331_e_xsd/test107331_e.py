from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


@dataclass(kw_only=True)
class Ct1:
    class Meta:
        name = "ct1"

    value: None | object = field(default=None)


@dataclass(kw_only=True)
class Ct3:
    class Meta:
        name = "ct3"

    elem: None | object = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


class Ct4State(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


@dataclass(kw_only=True)
class Item:
    class Meta:
        name = "item"

    value: None | object = field(default=None)


@dataclass(kw_only=True)
class A(Ct1):
    class Meta:
        name = "a"


@dataclass(kw_only=True)
class Ct2(Ct1):
    class Meta:
        name = "ct2"


@dataclass(kw_only=True)
class Ct4:
    class Meta:
        name = "ct4"

    value: str = field(default="")
    name: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    type_value: int = field(
        metadata={
            "name": "type",
            "type": "Attribute",
        }
    )
    state: Ct4State = field(
        metadata={
            "type": "Attribute",
        }
    )


@dataclass(kw_only=True)
class B(Ct2):
    class Meta:
        name = "b"


@dataclass(kw_only=True)
class C(Ct4):
    class Meta:
        name = "c"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    choice: list[C | B | A | Item] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "c",
                    "type": C,
                },
                {
                    "name": "b",
                    "type": B,
                },
                {
                    "name": "a",
                    "type": A,
                },
                {
                    "name": "item",
                    "type": Item,
                },
            ),
        },
    )
