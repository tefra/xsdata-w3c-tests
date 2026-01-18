from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal


@dataclass(kw_only=True)
class Number:
    class Meta:
        name = "number"

    value: Decimal = field(
        metadata={
            "required": True,
        }
    )
