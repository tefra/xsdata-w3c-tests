from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional


@dataclass
class Root:
    """
    :ivar value:
    :ivar type:
    """
    class Meta:
        name = "root"

    value: Optional[Decimal] = field(
        default=None,
    )
    type: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/2001/XMLSchema-instance"
        )
    )
