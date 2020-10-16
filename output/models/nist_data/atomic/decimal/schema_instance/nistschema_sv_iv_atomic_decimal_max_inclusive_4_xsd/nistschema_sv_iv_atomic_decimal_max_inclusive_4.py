from dataclasses import dataclass, field
from decimal import Decimal
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
        metadata={
            "required": True,
            "max_inclusive": -95776055693671313,
        }
    )
