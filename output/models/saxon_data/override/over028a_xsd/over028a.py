from dataclasses import dataclass, field
from typing import Optional


@dataclass
class NewSize:
    class Meta:
        name = "newSize"

    value: Optional[int] = field(
        default=None,
        metadata={
            "max_inclusive": 16,
        }
    )
