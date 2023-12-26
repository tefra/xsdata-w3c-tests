from dataclasses import dataclass, field
from typing import List


@dataclass
class N:
    class Meta:
        name = "n"

    value: str = field(default="")


@dataclass
class Outer:
    class Meta:
        name = "outer"

    n: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
