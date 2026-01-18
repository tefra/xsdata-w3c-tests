from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-maxInclusive-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDecimalMaxInclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-maxInclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-decimal-maxInclusive-5-NS"

    value: Decimal = field(
        metadata={
            "required": True,
            "max_inclusive": Decimal("999999999999999999"),
        }
    )
