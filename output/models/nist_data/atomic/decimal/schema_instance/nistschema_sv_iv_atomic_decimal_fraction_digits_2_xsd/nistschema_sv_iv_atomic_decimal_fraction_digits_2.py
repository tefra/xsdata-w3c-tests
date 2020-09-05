from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-fractionDigits-2-NS"


@dataclass
class NistschemaSvIvAtomicDecimalFractionDigits2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-fractionDigits-2"
        namespace = "NISTSchema-SV-IV-atomic-decimal-fractionDigits-2-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            required=True,
            fraction_digits=4
        )
    )
