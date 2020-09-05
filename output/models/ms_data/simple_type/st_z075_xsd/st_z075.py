from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "a"


class Type(Enum):
    """
    :cvar X:
    """
    X = "x"


@dataclass
class Doc:
    """
    :ivar value:
    """
    class Meta:
        name = "doc"
        namespace = "a"

    value: Optional[Type] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
