from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional


@dataclass
class Root:
    """
    :ivar value:
    """
    class Meta:
        name = "root"

    value: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            required=True,
            min_exclusive=5
        )
    )
