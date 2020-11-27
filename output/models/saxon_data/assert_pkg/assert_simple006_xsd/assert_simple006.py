from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Outer:
    class Meta:
        name = "outer"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Value:
    class Meta:
        name = "value"

    value: Optional[str] = field(
        default=None,
    )
