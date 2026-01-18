from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class FooType(Enum):
    CA = "CA"
    OR = "OR"


@dataclass(kw_only=True)
class FooTest:
    class Meta:
        name = "fooTest"

    value: FooType = field(
        metadata={
            "required": True,
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
            "required": True,
        }
    )
