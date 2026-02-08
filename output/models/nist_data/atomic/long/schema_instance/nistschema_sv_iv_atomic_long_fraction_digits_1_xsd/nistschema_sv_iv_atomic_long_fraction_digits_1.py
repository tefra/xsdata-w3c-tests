from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-long-fractionDigits-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicLongFractionDigits1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-long-fractionDigits-1"
        namespace = "NISTSchema-SV-IV-atomic-long-fractionDigits-1-NS"

    value: int = field(
        metadata={
            "fraction_digits": 0,
        }
    )
