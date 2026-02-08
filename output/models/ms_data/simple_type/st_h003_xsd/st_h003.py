from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class ListOfStatesValue(Enum):
    WA = "WA"
    OR = "OR"
    CA = "CA"


@dataclass(kw_only=True)
class FooTest:
    class Meta:
        name = "fooTest"

    value: list[ListOfStatesValue | str] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
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
