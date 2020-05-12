from enum import Enum
from dataclasses import dataclass, field
from typing import List


class U3(Enum):
    """
    :cvar X:
    :cvar Y:
    :cvar VALUE_1:
    """
    X = "x"
    Y = "y"
    VALUE_1 = "1"


@dataclass
class Root:
    """
    :ivar c:
    """
    class Meta:
        name = "root"

    c: List[U3] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="",
            min_occurs=0,
            max_occurs=40
        )
    )
