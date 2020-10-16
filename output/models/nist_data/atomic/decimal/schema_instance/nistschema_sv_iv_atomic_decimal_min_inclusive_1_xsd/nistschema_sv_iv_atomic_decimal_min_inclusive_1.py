from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-minInclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicDecimalMinInclusive1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-minInclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-decimal-minInclusive-1-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": -999999999999999999,
        }
    )
