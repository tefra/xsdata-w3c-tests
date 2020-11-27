from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class A(Enum):
    B = "B𠀀"


@dataclass
class DKstra:
    class Meta:
        name = "Dĳkstra"

    a: Optional[A] = field(
        default=None,
        metadata={
            "name": "A𰀀",
            "type": "Attribute",
        }
    )
