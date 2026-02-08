from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-minInclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDecimalMinInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-minInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-decimal-minInclusive-2-NS"

    value: Decimal = field(
        metadata={
            "min_inclusive": Decimal("229822855408968073"),
        }
    )
