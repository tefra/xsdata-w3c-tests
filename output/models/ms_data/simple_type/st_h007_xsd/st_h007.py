from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class ListOfStatesValue(Enum):
    CA = "CA"
    OR = "OR"
    WA = "WA"


class FooType(Enum):
    CA = "CA"


@dataclass
class FooTest:
    class Meta:
        name = "fooTest"

    value: Optional[FooType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    foo_test: Optional[FooType] = field(
        default=None,
        metadata={
            "name": "fooTest",
            "type": "Element",
            "required": True,
        }
    )
