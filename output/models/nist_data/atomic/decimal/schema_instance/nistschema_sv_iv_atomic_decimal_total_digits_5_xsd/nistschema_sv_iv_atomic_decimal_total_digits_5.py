from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-totalDigits-5-NS"


@dataclass
class NistschemaSvIvAtomicDecimalTotalDigits5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-totalDigits-5"
        namespace = "NISTSchema-SV-IV-atomic-decimal-totalDigits-5-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "total_digits": 18,
        }
    )
