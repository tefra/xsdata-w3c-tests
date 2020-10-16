from dataclasses import dataclass, field
from decimal import Decimal
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
        metadata={
            "required": True,
            "max_inclusive": 625897845365533055,
        }
    )
