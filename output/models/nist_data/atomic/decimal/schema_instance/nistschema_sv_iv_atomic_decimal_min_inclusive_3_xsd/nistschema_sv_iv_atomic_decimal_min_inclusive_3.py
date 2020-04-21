from decimal import Decimal
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-minInclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicDecimalMinInclusive3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-minInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-decimal-minInclusive-3-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            required=True,
            min_inclusive=-7.85368448026986e+17
        )
    )
