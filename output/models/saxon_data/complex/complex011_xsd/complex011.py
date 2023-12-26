from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional


@dataclass
class Root:
    class Meta:
        name = "root"
        nillable = True

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "nillable": True,
        },
    )
    present: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
