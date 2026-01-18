from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-integer-totalDigits-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicIntegerTotalDigits3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-integer-totalDigits-3"
        namespace = "NISTSchema-SV-IV-atomic-integer-totalDigits-3-NS"

    value: int = field(
        metadata={
            "required": True,
            "total_digits": 9,
        }
    )
