from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-fractionDigits-3-NS"


@dataclass
class NistschemaSvIvAtomicDecimalFractionDigits3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-fractionDigits-3"
        namespace = "NISTSchema-SV-IV-atomic-decimal-fractionDigits-3-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "fraction_digits": 8,
        },
    )
