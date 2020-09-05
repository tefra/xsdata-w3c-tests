from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-maxInclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicDecimalMaxInclusive1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-maxInclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-decimal-maxInclusive-1-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            required=True,
            max_inclusive=-999999999999999999
        )
    )
