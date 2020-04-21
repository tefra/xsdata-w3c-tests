from decimal import Decimal
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Root:
    """
    :ivar value:
    :ivar nil:
    """
    class Meta:
        name = "root"
        nillable = True

    value: Optional[Decimal] = field(
        default=None,
    )
    nil: str = field(
        default="true",
        metadata=dict(
            type="Attribute",
            namespace="http://www.w3.org/2001/XMLSchema-instance"
        )
    )
