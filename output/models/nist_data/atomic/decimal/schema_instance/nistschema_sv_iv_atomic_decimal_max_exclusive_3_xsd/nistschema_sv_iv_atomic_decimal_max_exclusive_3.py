from decimal import Decimal
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicDecimalMaxExclusive3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-3-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            required=True,
            max_exclusive=1.71942968603658e+17
        )
    )