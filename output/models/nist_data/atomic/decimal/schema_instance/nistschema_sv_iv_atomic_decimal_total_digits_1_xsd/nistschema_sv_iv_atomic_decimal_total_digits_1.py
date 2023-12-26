from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-totalDigits-1-NS"


@dataclass
class NistschemaSvIvAtomicDecimalTotalDigits1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-totalDigits-1"
        namespace = "NISTSchema-SV-IV-atomic-decimal-totalDigits-1-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "total_digits": 1,
        },
    )
