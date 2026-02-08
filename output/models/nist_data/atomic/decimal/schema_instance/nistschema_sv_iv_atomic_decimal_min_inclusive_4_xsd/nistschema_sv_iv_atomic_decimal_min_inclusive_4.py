from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-minInclusive-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDecimalMinInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-minInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-decimal-minInclusive-4-NS"

    value: Decimal = field(
        metadata={
            "min_inclusive": Decimal("325207740352921658"),
        }
    )
