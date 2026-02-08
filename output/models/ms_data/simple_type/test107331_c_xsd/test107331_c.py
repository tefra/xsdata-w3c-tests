from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class A1(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


@dataclass(kw_only=True)
class A2:
    class Meta:
        name = "A"

    value: int = field(
        metadata={
            "min_exclusive": 0,
            "max_inclusive": 10,
        }
    )


class B1(Enum):
    A = "a"
    B = "b"
    C123456789 = "c123456789"


@dataclass(kw_only=True)
class B2:
    class Meta:
        name = "B"

    value: str = field(
        default="",
        metadata={
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


@dataclass(kw_only=True)
class Item:
    class Meta:
        name = "item"

    value: None | object = field(default=None)


@dataclass(kw_only=True)
class A3:
    class Meta:
        name = "a"

    value: A1 = field()


@dataclass(kw_only=True)
class B3:
    class Meta:
        name = "b"

    value: B1 = field()


@dataclass(kw_only=True)
class La:
    class Meta:
        name = "la"

    value: list[A1] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class Lab:
    class Meta:
        name = "lab"

    value: list[UnionAb] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class Ra:
    class Meta:
        name = "ra"

    value: RA1 = field()


@dataclass(kw_only=True)
class Ua:
    class Meta:
        name = "ua"

    value: UnionA = field()


@dataclass(kw_only=True)
class Uab:
    class Meta:
        name = "uab"

    value: UnionAb = field()


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    choice: list[Ra | Lab | La | Uab | Ua | B3 | A3 | B2 | A2 | Item] = field(
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
