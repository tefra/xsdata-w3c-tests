from decimal import Decimal
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Number:
    """
    :ivar value:
    """
    class Meta:
        name = "number"

    value: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
