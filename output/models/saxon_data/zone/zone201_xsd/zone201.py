from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Doc:
    class Meta:
        name = "doc"

    value: Optional[datetime] = field(
        default=None,
        metadata={
            "min_inclusive": "0000-01-01T12:00:00",
        }
    )
