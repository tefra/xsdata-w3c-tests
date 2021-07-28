from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-minInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicDecimalMinInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-minInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-decimal-minInclusive-4-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("325207740352921658"),
        }
    )
