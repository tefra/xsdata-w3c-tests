from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional


@dataclass
class Foo:
    class Meta:
        name = "foo"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "total_digits": 5,
            "fraction_digits": 2,
        }
    )
