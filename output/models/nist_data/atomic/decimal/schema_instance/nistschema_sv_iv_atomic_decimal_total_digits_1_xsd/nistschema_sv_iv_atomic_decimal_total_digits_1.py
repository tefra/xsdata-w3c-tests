from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-totalDigits-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDecimalTotalDigits1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-totalDigits-1"
        namespace = "NISTSchema-SV-IV-atomic-decimal-totalDigits-1-NS"

    value: Decimal = field(
        metadata={
            "total_digits": 1,
        }
    )
