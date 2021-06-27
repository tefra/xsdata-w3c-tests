from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional


@dataclass
class T1:
    class Meta:
        name = "t1"

    att9: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "total_digits": 5,
            "fraction_digits": 5,
        }
    )
