from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-minExclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicDecimalMinExclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-minExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-decimal-minExclusive-5-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": Decimal("999999999999999998"),
        }
    )
