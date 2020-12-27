from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class Doc:
    class Meta:
        name = "doc"

    para: List[datetime] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
