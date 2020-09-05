from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


@dataclass
class MyType:
    """
    :ivar value:
    """
    class Meta:
        name = "myType"

    value: Optional[str] = field(
        default=None,
    )


class FooType(Enum):
    """
    :cvar CA:
    """
    CA = "CA"


@dataclass
class Root:
    """
    :ivar value:
    """
    class Meta:
        name = "root"

    value: Optional[FooType] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
