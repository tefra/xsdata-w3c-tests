from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class UnionA(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


@dataclass
class Test:
    class Meta:
        name = "test"

    value: Optional[UnionA] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    test: list[Test] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
