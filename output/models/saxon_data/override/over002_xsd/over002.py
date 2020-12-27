from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class Para:
    class Meta:
        name = "para"

    value: Optional[datetime] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
