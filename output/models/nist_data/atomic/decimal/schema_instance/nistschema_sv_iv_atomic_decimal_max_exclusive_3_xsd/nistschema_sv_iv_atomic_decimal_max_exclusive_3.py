from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicDecimalMaxExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-3-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": Decimal("171942968603657986"),
        },
    )
