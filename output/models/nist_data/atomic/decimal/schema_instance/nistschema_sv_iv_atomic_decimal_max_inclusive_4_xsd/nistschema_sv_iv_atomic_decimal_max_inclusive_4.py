from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-maxInclusive-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDecimalMaxInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-maxInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-decimal-maxInclusive-4-NS"

    value: Decimal = field(
        metadata={
            "required": True,
            "max_inclusive": Decimal("-95776055693671313"),
        }
    )
