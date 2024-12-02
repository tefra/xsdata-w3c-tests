from dataclasses import dataclass, field
from enum import Enum

__NAMESPACE__ = "a"


class Num1(Enum):
    INF = float("inf")
    VALUE_1_1 = 1.1


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "a"

    number1: list[Num1] = field(
        default_factory=list,
        metadata={
            "name": "Number1",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    number2: list[float] = field(
        default_factory=list,
        metadata={
            "name": "Number2",
            "type": "Element",
            "min_occurs": 1,
        },
    )
