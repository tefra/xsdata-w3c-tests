from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class UnionAb(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    A = "a"
    B = "b"
    C123456789 = "c123456789"


@dataclass
class Root:
    class Meta:
        name = "root"

    test: List[UnionAb] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
class Test:
    class Meta:
        name = "test"

    value: Optional[UnionAb] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
