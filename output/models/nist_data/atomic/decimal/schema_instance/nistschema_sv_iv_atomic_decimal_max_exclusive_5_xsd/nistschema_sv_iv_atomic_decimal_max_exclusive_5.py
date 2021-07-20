from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicDecimalMaxExclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-5-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "max_exclusive": Decimal("999999999999999999"),
        }
    )
