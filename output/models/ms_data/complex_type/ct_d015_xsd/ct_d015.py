from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


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
        metadata={
            "required": True,
        }
    )
