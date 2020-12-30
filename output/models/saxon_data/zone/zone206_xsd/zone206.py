from dataclasses import dataclass, field
from datetime import time
from typing import List, Optional


@dataclass
class Doc:
    class Meta:
        name = "doc"

    target: Optional[time] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    equiv: List[time] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
