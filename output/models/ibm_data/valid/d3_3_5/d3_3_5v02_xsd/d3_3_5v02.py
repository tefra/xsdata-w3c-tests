from enum import Enum
from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "a"


class Num1(Enum):
    """
    :cvar INF:
    :cvar VALUE_1_1:
    """
    INF = "+INF"
    VALUE_1_1 = "1.1"


@dataclass
class Root:
    """
    :ivar number1:
    :ivar number2:
    """
    class Meta:
        name = "root"
        namespace = "a"

    number1: List[Num1] = field(
        default_factory=list,
        metadata=dict(
            name="Number1",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
    number2: List[float] = field(
        default_factory=list,
        metadata=dict(
            name="Number2",
            type="Element",
            min_occurs=1,
            max_occurs=9223372036854775807
        )
    )
