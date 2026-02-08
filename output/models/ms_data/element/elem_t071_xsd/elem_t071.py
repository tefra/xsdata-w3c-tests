from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class UnionA(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


@dataclass(kw_only=True)
class Test:
    class Meta:
        name = "test"

    value: UnionA = field()


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
