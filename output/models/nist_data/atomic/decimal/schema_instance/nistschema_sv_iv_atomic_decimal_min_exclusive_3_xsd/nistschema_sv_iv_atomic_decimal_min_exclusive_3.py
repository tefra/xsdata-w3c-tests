from decimal import Decimal
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-minExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicDecimalMinExclusive3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-minExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-decimal-minExclusive-3-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            required=True,
            min_exclusive=-6.74282596046889e+16
        )
    )