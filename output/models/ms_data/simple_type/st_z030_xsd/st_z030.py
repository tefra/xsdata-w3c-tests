from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Ct:
    class Meta:
        name = "ct"

    e1: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_exclusive": 2,
            "min_inclusive": 2,
        }
    )
    e2: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_exclusive": 2,
            "min_inclusive": 3,
        }
    )


@dataclass
class Root(Ct):
    pass
