from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class A(Enum):
    """
    :cvar B:
    """
    B = "B𠀀"


@dataclass
class DKstra:
    """
    :ivar a:
    """
    class Meta:
        name = "Dĳkstra"

    a: Optional[A] = field(
        default=None,
        metadata=dict(
            name="A𰀀",
            type="Attribute"
        )
    )
