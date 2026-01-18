from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-fractionDigits-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDecimalFractionDigits4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-fractionDigits-4"
        namespace = "NISTSchema-SV-IV-atomic-decimal-fractionDigits-4-NS"

    value: Decimal = field(
        metadata={
            "required": True,
            "fraction_digits": 12,
        }
    )
