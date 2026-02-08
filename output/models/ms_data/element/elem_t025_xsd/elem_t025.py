from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class A(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


@dataclass(kw_only=True)
class Ca:
    class Meta:
        name = "CA"

    x: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 2,
        },
    )
    y: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass(kw_only=True)
class SA:
    class Meta:
        name = "s-a"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class ECa(Ca):
    class Meta:
        name = "E-CA"

    z: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass(kw_only=True)
class RCa(Ca):
    class Meta:
        name = "R-CA"

    y: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    x: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )


@dataclass(kw_only=True)
class Test:
    class Meta:
        name = "test"

    value: A = field()


@dataclass(kw_only=True)
class Test2(Ca):
    class Meta:
        name = "test2"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    s_a_or_test: None | SA | Test = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "s-a",
                    "type": SA,
                },
                {
                    "name": "test",
                    "type": Test,
                },
            ),
        },
    )
    test2: None | Test2 = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
