from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-minExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicDecimalMinExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-minExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-decimal-minExclusive-4-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": Decimal("-294253147230818967"),
        },
    )
