from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    value: list[float | Decimal | int] = field(
        init=False,
        default_factory=lambda: [
            12,
            1.278656273654,
            4.0,
        ],
        metadata={
            "tokens": True,
        },
    )
