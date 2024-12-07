from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, Union


@dataclass
class Ct1:
    class Meta:
        name = "ct1"

    value: Optional[object] = field(default=None)


@dataclass
class Ct3:
    class Meta:
        name = "ct3"

    elem: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


class Ct4State(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2


@dataclass
class Item:
    class Meta:
        name = "item"

    value: Optional[object] = field(default=None)


@dataclass
class A(Ct1):
    class Meta:
        name = "a"


@dataclass
class Ct2(Ct1):
    class Meta:
        name = "ct2"


@dataclass
class Ct4:
    class Meta:
        name = "ct4"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    type_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )
    state: Optional[Ct4State] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class B(Ct2):
    class Meta:
        name = "b"


@dataclass
class C(Ct4):
    class Meta:
        name = "c"


@dataclass
class Root:
    class Meta:
        name = "root"

    choice: list[Union[C, B, A, Item]] = field(
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
