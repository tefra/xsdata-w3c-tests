from dataclasses import dataclass, field
from enum import Enum
from typing import List, Union


@dataclass
class FooTest:
    class Meta:
        name = "fooTest"

    value: List[Union[int, "FooTest.Value"]] = field(
        default_factory=list,
        metadata={
            "required": True,
            "tokens": True,
        }
    )

    class Value(Enum):
        WA = "WA"
        OR_VALUE = "OR"


@dataclass
class Root:
    class Meta:
        name = "root"

    foo_test: List[Union[int, "Root.Value"]] = field(
        default_factory=list,
        metadata={
            "name": "fooTest",
            "type": "Element",
            "required": True,
            "tokens": True,
        }
    )

    class Value(Enum):
        WA = "WA"
        OR_VALUE = "OR"
