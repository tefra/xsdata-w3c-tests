from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-maxInclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicDecimalMaxInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-maxInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-decimal-maxInclusive-3-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": Decimal("-888403528420030673"),
        }
    )
