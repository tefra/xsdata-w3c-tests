from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonPositiveInteger-totalDigits-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNonPositiveIntegerTotalDigits5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonPositiveInteger-totalDigits-5"
        namespace = (
            "NISTSchema-SV-IV-atomic-nonPositiveInteger-totalDigits-5-NS"
        )

    value: int = field(
        metadata={
            "total_digits": 18,
        }
    )
