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
        }
    )
    section: list[Section] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    id: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
    nr: Decimal = field(
        metadata={
            "type": "Attribute",
        }
    )
