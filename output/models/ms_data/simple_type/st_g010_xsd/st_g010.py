from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class FooType(Enum):
    """
    :cvar CA:
    :cvar OR_VALUE:
    """
    CA = "CA"
    OR_VALUE = "OR"


@dataclass
class FooTest:
    """
    :ivar value:
    """
    class Meta:
        name = "fooTest"

    value: Optional[FooType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Root:
    """
    :ivar foo_test:
    """
    class Meta:
        name = "root"

    foo_test: Optional[FooType] = field(
        default=None,
        metadata={
            "name": "fooTest",
            "type": "Element",
            "required": True,
        }
    )
