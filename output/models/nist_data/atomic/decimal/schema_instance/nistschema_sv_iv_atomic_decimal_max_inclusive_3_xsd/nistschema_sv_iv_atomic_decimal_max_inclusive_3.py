from decimal import Decimal
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-maxInclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicDecimalMaxInclusive3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-maxInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-decimal-maxInclusive-3-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            required=True,
            max_inclusive=-8.884035284200307e+17
        )
    )
