from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Date:
    class Meta:
        name = "date"

    value: Optional[str] = field(
        default=None,
    )


@dataclass
class Outer:
    class Meta:
        name = "outer"

    date: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
