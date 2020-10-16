from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-fractionDigits-4-NS"


@dataclass
class NistschemaSvIvAtomicDecimalFractionDigits4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-fractionDigits-4"
        namespace = "NISTSchema-SV-IV-atomic-decimal-fractionDigits-4-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "fraction_digits": 12,
        }
    )
