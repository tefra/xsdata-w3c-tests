from decimal import Decimal
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-minInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicDecimalMinInclusive4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-minInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-decimal-minInclusive-4-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            required=True,
            min_inclusive=3.2520774035292166e+17
        )
    )
