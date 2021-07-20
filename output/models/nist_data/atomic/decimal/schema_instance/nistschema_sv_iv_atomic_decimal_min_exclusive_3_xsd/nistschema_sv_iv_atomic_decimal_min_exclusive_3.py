from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-minExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicDecimalMinExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-minExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-decimal-minExclusive-3-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "min_exclusive": Decimal("-67428259604688900"),
        }
    )
