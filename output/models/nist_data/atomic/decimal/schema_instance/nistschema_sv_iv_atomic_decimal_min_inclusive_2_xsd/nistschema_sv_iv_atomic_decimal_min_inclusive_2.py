from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-minInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicDecimalMinInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-minInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-decimal-minInclusive-2-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("229822855408968073"),
        },
    )
