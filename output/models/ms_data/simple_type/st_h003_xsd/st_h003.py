from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional, Union


class ListOfStates(Enum):
    """
    :cvar WA:
    :cvar OR_VALUE:
    :cvar CA:
    """
    WA = "WA"
    OR_VALUE = "OR"
    CA = "CA"


@dataclass
class FooTest:
    """
    :ivar value:
    """
    class Meta:
        name = "fooTest"

    value: List[Union[ListOfStates, str]] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Root:
    """
    :ivar foo_test:
    """
    class Meta:
        name = "root"

    foo_test: Optional[FooTest] = field(
        default=None,
        metadata=dict(
            name="fooTest",
            type="Element",
            required=True
        )
    )
