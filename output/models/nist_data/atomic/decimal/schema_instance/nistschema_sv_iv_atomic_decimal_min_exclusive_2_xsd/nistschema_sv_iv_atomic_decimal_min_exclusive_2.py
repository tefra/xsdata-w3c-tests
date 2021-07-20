from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-minExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicDecimalMinExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-minExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-decimal-minExclusive-2-NS"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "min_exclusive": Decimal("631308414640570968"),
        }
    )
