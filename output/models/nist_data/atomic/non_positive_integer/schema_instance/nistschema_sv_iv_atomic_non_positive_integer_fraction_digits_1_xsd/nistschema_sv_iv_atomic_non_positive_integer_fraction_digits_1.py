from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = (
    "NISTSchema-SV-IV-atomic-nonPositiveInteger-fractionDigits-1-NS"
)


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNonPositiveIntegerFractionDigits1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonPositiveInteger-fractionDigits-1"
        namespace = (
            "NISTSchema-SV-IV-atomic-nonPositiveInteger-fractionDigits-1-NS"
        )

    value: int = field(
        metadata={
            "required": True,
            "fraction_digits": 0,
        }
    )
