from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-maxInclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDecimalMaxInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-maxInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-decimal-maxInclusive-3-NS"

    value: Decimal = field(
        metadata={
            "max_inclusive": Decimal("-888403528420030673"),
        }
    )
