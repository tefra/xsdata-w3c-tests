from dataclasses import dataclass, field
from enum import Enum
from typing import List, Union


class MyUnionValue(Enum):
    WA = "WA"
    OR = "OR"


@dataclass
class FooTest:
    class Meta:
        name = "fooTest"

    value: List[Union[int, MyUnionValue]] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    foo_test: List[Union[int, MyUnionValue]] = field(
        default_factory=list,
        metadata={
            "name": "fooTest",
            "type": "Element",
            "required": True,
            "tokens": True,
        }
    )
