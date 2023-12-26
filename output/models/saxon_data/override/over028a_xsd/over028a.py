from dataclasses import dataclass, field
from typing import Optional


@dataclass
class NewSize:
    class Meta:
        name = "newSize"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": 16,
        },
    )
