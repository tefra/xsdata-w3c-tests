from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class UnionAb(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    A = "a"
    B = "b"
    C123456789 = "c123456789"


@dataclass(kw_only=True)
class Test:
    class Meta:
        name = "test"

    value: UnionAb = field()


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    test: list[Test] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
