from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-maxInclusive-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDecimalMaxInclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-maxInclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-decimal-maxInclusive-1-NS"

    value: Decimal = field(
        metadata={
            "max_inclusive": Decimal("-999999999999999999"),
        }
    )
