from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal


@dataclass(kw_only=True)
class Section:
    class Meta:
        name = "section"

    head: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    section: list[Section] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    nr: Decimal = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
