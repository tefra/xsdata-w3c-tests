from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicDecimalMaxExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-decimal-maxExclusive-2-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": Decimal("78119693427168402"),
        },
    )
