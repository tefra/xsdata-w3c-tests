from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedLong-totalDigits-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedLongTotalDigits3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedLong-totalDigits-3"
        namespace = "NISTSchema-SV-IV-atomic-unsignedLong-totalDigits-3-NS"

    value: int = field(
        metadata={
            "total_digits": 9,
        }
    )
