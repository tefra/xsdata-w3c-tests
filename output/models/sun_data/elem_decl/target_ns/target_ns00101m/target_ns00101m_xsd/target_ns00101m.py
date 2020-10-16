from dataclasses import dataclass, field
from decimal import Decimal
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
        metadata={
            "required": True,
        }
    )
