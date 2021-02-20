from dataclasses import dataclass, field
from enum import Enum
from typing import List, Union


class ListOfStatesValue(Enum):
    WA = "WA"
    OR_VALUE = "OR"
    CA = "CA"


@dataclass
class FooTest:
    class Meta:
        name = "fooTest"

    value: List[Union[ListOfStatesValue, str]] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    foo_test: List[Union[ListOfStatesValue, str]] = field(
        default_factory=list,
        metadata={
            "name": "fooTest",
            "type": "Element",
            "tokens": True,
        }
    )
