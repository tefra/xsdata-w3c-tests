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
            "explicit_timezone": "required",
        }
    )
