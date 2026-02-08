from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-minInclusive-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDecimalMinInclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-minInclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-decimal-minInclusive-1-NS"

    value: Decimal = field(
        metadata={
            "min_inclusive": Decimal("-999999999999999999"),
        }
    )
