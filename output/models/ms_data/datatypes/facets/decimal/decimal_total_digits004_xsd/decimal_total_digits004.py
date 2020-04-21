from decimal import Decimal
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class T1:
    """
    :ivar att9:
    """
    class Meta:
        name = "t1"

    att9: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            required=True,
            total_digits=5,
            fraction_digits=5
        )
    )
