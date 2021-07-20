from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class A(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


class B(Enum):
    A = "a"
    B = "b"
    C123456789 = "c123456789"


class RA(Enum):
    VALUE_1 = 1
    VALUE_2 = 2


class UnionA(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


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

    test: List[UnionA] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Test:
    class Meta:
        name = "test"

    value: Optional[UnionA] = field(
        default=None
    )
