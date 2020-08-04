from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional, Union


@dataclass
class FooTest:
    """
    :ivar value:
    """
    class Meta:
        name = "fooTest"

    value: List[Union["FooTest.Value", str]] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            tokens=True
        )
    )

    class Value(Enum):
        """
        :cvar WA:
        :cvar OR_VALUE:
        :cvar CA:
        """
        WA = "WA"
        OR_VALUE = "OR"
        CA = "CA"


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
