from decimal import Decimal
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicDecimalMaxExclusive4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-4-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata=dict(
            required=True,
            max_exclusive=-2.1477192619072438e+17
        )
    )