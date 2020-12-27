from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional


@dataclass
class Doc:
    class Meta:
        name = "doc"

    value: Optional[datetime] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": datetime(2000, 1, 1, 0, 0, tzinfo=timezone.utc),
            "max_inclusive": datetime(2999, 12, 31, 23, 59, 59, tzinfo=timezone.utc),
        }
    )
