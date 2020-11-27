from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Doc:
    class Meta:
        name = "doc"

    target: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    equiv: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
