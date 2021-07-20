from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional


@dataclass
class Number:
    class Meta:
        name = "number"

    value: Optional[Decimal] = field(
        default=None
    )
