from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonPositiveInteger-totalDigits-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNonPositiveIntegerTotalDigits4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonPositiveInteger-totalDigits-4"
        namespace = (
            "NISTSchema-SV-IV-atomic-nonPositiveInteger-totalDigits-4-NS"
        )

    value: int = field(
        metadata={
            "required": True,
            "total_digits": 13,
        }
    )
