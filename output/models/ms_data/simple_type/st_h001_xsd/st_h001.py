from dataclasses import dataclass, field
from enum import Enum
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
        metadata={
            "required": True,
            "min_inclusive": 100,
            "max_inclusive": 200,
        }
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

    foo_test: Optional[Union[int, "Root.Value"]] = field(
        default=None,
        metadata={
            "name": "fooTest",
            "type": "Element",
            "required": True,
            "min_inclusive": 100,
            "max_inclusive": 200,
        }
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
