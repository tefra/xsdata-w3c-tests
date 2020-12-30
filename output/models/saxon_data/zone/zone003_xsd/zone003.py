from dataclasses import dataclass, field
from datetime import time
from typing import Optional


@dataclass
class Doc:
    class Meta:
        name = "doc"

    value: Optional[time] = field(
        default=None,
        metadata={
            "explicit_timezone": "optional",
        }
    )
