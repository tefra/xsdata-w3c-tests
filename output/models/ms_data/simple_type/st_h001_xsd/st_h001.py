from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, Union


@dataclass
class FooTest:
    class Meta:
        name = "fooTest"

    value: Optional[Union[int, "FooTest.Value"]] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": 100,
            "max_inclusive": 200,
        }
    )

    class Value(Enum):
        WA = "WA"
        OR_VALUE = "OR"
        CA = "CA"


@dataclass
class Root:
    class Meta:
        name = "root"

    foo_test: Optional[Union[int, "Root.FooTest"]] = field(
        default=None,
        metadata={
            "name": "fooTest",
            "type": "Element",
            "required": True,
            "min_inclusive": 100,
            "max_inclusive": 200,
        }
    )

    class FooTest(Enum):
        WA = "WA"
        OR_VALUE = "OR"
        CA = "CA"
