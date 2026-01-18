from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class StructuredDate:
    class Meta:
        name = "structuredDate"

    year: int = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    month: int = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    day: int = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
