from decimal import Decimal
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-maxInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicDecimalMaxInclusive2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-maxInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-decimal-maxInclusive-2-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            required=True,
            max_inclusive=6.25897845365533e+17
        )
    )
