from decimal import Decimal
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-fractionDigits-5-NS"


@dataclass
class NistschemaSvIvAtomicDecimalFractionDigits5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-fractionDigits-5"
        namespace = "NISTSchema-SV-IV-atomic-decimal-fractionDigits-5-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            required=True,
            fraction_digits=18
        )
    )