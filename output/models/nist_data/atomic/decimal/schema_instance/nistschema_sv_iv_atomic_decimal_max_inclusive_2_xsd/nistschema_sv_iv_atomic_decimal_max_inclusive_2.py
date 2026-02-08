from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-maxInclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDecimalMaxInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-maxInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-decimal-maxInclusive-2-NS"

    value: Decimal = field(
        metadata={
            "max_inclusive": Decimal("625897845365533055"),
        }
    )
