from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-minExclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicDecimalMinExclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-minExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-decimal-minExclusive-1-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": Decimal("-999999999999999999"),
        },
    )
