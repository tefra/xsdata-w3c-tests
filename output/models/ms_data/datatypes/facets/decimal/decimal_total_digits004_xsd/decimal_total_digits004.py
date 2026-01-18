from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal


@dataclass(kw_only=True)
class T1:
    class Meta:
        name = "t1"

    att9: None | Decimal = field(
        default=None,
        metadata={
            "type": "Attribute",
            "total_digits": 5,
            "fraction_digits": 5,
        },
    )
