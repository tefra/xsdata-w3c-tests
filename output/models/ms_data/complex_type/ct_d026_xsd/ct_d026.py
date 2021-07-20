from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional


@dataclass
class Root:
    class Meta:
        name = "root"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "fraction_digits": 5,
        }
    )
