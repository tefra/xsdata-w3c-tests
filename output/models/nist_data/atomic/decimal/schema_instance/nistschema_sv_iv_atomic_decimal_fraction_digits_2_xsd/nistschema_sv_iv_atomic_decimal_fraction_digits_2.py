from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-decimal-fractionDigits-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicDecimalFractionDigits2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-decimal-fractionDigits-2"
        namespace = "NISTSchema-SV-IV-atomic-decimal-fractionDigits-2-NS"

    value: Decimal = field(
        metadata={
            "fraction_digits": 4,
        }
    )
