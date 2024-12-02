from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional


@dataclass
class Section:
    class Meta:
        name = "section"

    head: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    section: list["Section"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    nr: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
