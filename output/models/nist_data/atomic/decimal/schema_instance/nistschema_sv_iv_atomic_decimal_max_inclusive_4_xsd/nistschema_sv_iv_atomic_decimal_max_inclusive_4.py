from decimal import Decimal
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-maxInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicDecimalMaxInclusive4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-maxInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-decimal-maxInclusive-4-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            required=True,
            max_inclusive=-9.577605569367131e+16
        )
    )