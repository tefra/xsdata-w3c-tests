from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Message:
    class Meta:
        name = "message"

    value: Optional[str] = field(
        default=None,
        metadata={
            "max_length": 25,
        }
    )
