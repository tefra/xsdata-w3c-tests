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
    nil: str = field(
        default="true",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/2001/XMLSchema-instance",
        },
    )
