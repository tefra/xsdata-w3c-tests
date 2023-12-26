from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-minInclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicDecimalMinInclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-minInclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-decimal-minInclusive-5-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("999999999999999999"),
        },
    )
