from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicDecimalMaxExclusive1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-1-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": -999999999999999998,
        }
    )
