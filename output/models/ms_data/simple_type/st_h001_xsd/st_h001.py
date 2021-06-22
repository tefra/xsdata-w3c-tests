from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, Union


class FooTypeValue(Enum):
    WA = "WA"
    OR_VALUE = "OR"
    CA = "CA"


@dataclass
class FooTest:
    class Meta:
        name = "fooTest"

    value: Optional[Union[int, FooTypeValue]] = field(
        default=None,
        metadata={
            "min_inclusive": 100,
            "max_inclusive": 200,
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    foo_test: Optional[Union[int, FooTypeValue]] = field(
        default=None,
        metadata={
            "name": "fooTest",
            "type": "Element",
            "required": True,
            "min_inclusive": 100,
            "max_inclusive": 200,
        }
    )
