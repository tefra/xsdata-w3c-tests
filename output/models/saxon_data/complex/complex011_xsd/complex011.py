from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        nillable = True

    value: None | Decimal = field(
        metadata={
            "nillable": True,
        }
    )
    present: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
