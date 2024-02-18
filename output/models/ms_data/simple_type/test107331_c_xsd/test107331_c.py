from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union


class A1(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


@dataclass
class A2:
    class Meta:
        name = "A"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": 0,
            "max_inclusive": 10,
        },
    )


class B1(Enum):
    A = "a"
    B = "b"
    C123456789 = "c123456789"


@dataclass
class B2:
    class Meta:
        name = "B"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 0,
            "max_length": 10,
        },
    )


class RA1(Enum):
    VALUE_1 = 1
    VALUE_2 = 2


class UnionA(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


class UnionAb(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    A = "a"
    B = "b"
    C123456789 = "c123456789"


@dataclass
class Item:
    class Meta:
        name = "item"

    value: Optional[object] = field(default=None)


@dataclass
class A3:
    class Meta:
        name = "a"

    value: Optional[A1] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class B3:
    class Meta:
        name = "b"

    value: Optional[B1] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class La:
    class Meta:
        name = "la"

    value: List[A1] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )


@dataclass
class Lab:
    class Meta:
        name = "lab"

    value: List[UnionAb] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )


@dataclass
class Ra:
    class Meta:
        name = "ra"

    value: Optional[RA1] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Ua:
    class Meta:
        name = "ua"

    value: Optional[UnionA] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Uab:
    class Meta:
        name = "uab"

    value: Optional[UnionAb] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    choice: List[Union[Ra, Lab, La, Uab, Ua, B3, A3, B2, A2, Item]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ra",
                    "type": Ra,
                },
                {
                    "name": "lab",
                    "type": Lab,
                },
                {
                    "name": "la",
                    "type": La,
                },
                {
                    "name": "uab",
                    "type": Uab,
                },
                {
                    "name": "ua",
                    "type": Ua,
                },
                {
                    "name": "b",
                    "type": B3,
                },
                {
                    "name": "a",
                    "type": A3,
                },
                {
                    "name": "B",
                    "type": B2,
                },
                {
                    "name": "A",
                    "type": A2,
                },
                {
                    "name": "item",
                    "type": Item,
                },
            ),
        },
    )
