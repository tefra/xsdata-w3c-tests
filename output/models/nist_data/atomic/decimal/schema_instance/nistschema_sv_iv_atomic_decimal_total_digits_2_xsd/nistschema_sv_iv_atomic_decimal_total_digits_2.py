from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-totalDigits-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDecimalTotalDigits2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-totalDigits-2"
        namespace = "NISTSchema-SV-IV-atomic-decimal-totalDigits-2-NS"

    value: Decimal = field(
        metadata={
            "required": True,
            "total_digits": 5,
        }
    )
