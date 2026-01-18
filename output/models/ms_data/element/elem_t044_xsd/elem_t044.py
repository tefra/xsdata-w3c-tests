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
class Sa:
    class Meta:
        name = "sa"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Test4:
    class Meta:
        name = "test4"

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

    value: A = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Test2:
    class Meta:
        name = "test2"

    value: A = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Test3:
    class Meta:
        name = "test3"

    value: A = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    sa_or_test: None | Sa | Test = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "sa",
                    "type": Sa,
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
    test4: None | Test4 = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
