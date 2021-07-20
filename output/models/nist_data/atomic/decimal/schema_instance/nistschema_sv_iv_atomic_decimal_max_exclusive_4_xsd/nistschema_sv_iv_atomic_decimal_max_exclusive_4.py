from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicDecimalMaxExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-4-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "max_exclusive": Decimal("-214771926190724381"),
        }
    )
