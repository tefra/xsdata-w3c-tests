from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-totalDigits-3-NS"


@dataclass
class NistschemaSvIvAtomicDecimalTotalDigits3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-totalDigits-3"
        namespace = "NISTSchema-SV-IV-atomic-decimal-totalDigits-3-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "total_digits": 9,
        }
    )
