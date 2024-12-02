from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, Union


class ListOfStatesValue(Enum):
    WA = "WA"
    OR = "OR"
    CA = "CA"


@dataclass
class FooTest:
    class Meta:
        name = "fooTest"

    value: list[Union[ListOfStatesValue, str]] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    foo_test: Optional[FooTest] = field(
        default=None,
        metadata={
            "name": "fooTest",
            "type": "Element",
            "required": True,
        },
    )
