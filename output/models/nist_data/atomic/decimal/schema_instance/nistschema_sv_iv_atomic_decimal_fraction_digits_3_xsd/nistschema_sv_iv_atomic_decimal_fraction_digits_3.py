from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-fractionDigits-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDecimalFractionDigits3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-fractionDigits-3"
        namespace = "NISTSchema-SV-IV-atomic-decimal-fractionDigits-3-NS"

    value: Decimal = field(
        metadata={
            "fraction_digits": 8,
        }
    )
