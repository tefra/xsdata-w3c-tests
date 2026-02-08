from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class FooTypeValue(Enum):
    WA = "WA"
    OR = "OR"
    CA = "CA"


@dataclass(kw_only=True)
class FooTest:
    class Meta:
        name = "fooTest"

    value: int | FooTypeValue = field(
        metadata={
            "min_inclusive": 100,
            "max_inclusive": 200,
        }
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    foo_test: FooTest = field(
        metadata={
            "name": "fooTest",
            "type": "Element",
        }
    )
