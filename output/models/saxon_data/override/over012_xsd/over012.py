from dataclasses import dataclass, field
from typing import Optional


@dataclass
class StructuredDate:
    class Meta:
        name = "structuredDate"

    year: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    month: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    day: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
