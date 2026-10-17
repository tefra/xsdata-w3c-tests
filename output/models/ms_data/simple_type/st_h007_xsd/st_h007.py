from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum


class FooType(StrEnum):
    CA = "CA"


@dataclass(kw_only=True)
class FooTest:
    class Meta:
        name = "fooTest"

    value: FooType = field()


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
