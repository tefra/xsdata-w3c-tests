from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal


@dataclass(kw_only=True)
class Foo:
    class Meta:
        name = "foo"

    value: Decimal = field(
        metadata={
            "required": True,
            "total_digits": 5,
            "fraction_digits": 2,
        }
    )
