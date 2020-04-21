from enum import Enum
from dataclasses import dataclass, field
from typing import Optional, Union


@dataclass
class FooTest:
    """
    :ivar value:
    """
    class Meta:
        name = "fooTest"

    value: Optional[Union[int, "FooTest.Value"]] = field(
        default=None,
        metadata=dict(
            required=True,
            min_inclusive=100.0,
            max_inclusive=200.0
        )
    )

    class Value(Enum):
        """
        :cvar CA:
        :cvar OR_VALUE:
        :cvar WA:
        """
        CA = "CA"
        OR_VALUE = "OR"
        WA = "WA"


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
