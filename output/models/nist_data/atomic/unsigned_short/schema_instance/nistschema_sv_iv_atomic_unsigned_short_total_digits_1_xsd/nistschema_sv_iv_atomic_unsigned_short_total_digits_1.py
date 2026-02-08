from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedShort-totalDigits-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedShortTotalDigits1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedShort-totalDigits-1"
        namespace = "NISTSchema-SV-IV-atomic-unsignedShort-totalDigits-1-NS"

    value: int = field(
        metadata={
            "total_digits": 1,
        }
    )
