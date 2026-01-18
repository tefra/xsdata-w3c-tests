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
    nil: str = field(
        default="true",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/2001/XMLSchema-instance",
        },
    )
