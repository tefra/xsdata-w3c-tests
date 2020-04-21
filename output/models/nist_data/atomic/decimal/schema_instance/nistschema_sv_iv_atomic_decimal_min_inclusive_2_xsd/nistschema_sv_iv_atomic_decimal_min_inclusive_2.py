from decimal import Decimal
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-minInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicDecimalMinInclusive2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-minInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-decimal-minInclusive-2-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            required=True,
            min_inclusive=2.2982285540896806e+17
        )
    )
