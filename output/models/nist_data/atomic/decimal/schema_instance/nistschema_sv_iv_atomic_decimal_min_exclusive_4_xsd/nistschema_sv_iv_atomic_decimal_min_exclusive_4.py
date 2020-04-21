from decimal import Decimal
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-minExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicDecimalMinExclusive4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-minExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-decimal-minExclusive-4-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            required=True,
            min_exclusive=-2.9425314723081894e+17
        )
    )
