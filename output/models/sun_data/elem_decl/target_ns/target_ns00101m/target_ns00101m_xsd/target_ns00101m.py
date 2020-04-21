from decimal import Decimal
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ElemDecl/targetNS"


@dataclass
class Number:
    """
    :ivar value:
    """
    class Meta:
        name = "number"
        namespace = "ElemDecl/targetNS"

    value: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )
