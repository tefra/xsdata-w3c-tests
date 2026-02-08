from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


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
class Test:
    class Meta:
        name = "test"

    value: int = field(
        metadata={
            "min_exclusive": 0,
            "max_inclusive": 10,
        }
    )


@dataclass(kw_only=True)
class Test2:
    class Meta:
        name = "test2"

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
class Test3(Ca):
    class Meta:
        name = "test3"


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
    test3: None | Test3 = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
