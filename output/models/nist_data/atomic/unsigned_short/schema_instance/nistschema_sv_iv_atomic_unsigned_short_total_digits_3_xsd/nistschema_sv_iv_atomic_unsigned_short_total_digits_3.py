from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedShort-totalDigits-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedShortTotalDigits3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedShort-totalDigits-3"
        namespace = "NISTSchema-SV-IV-atomic-unsignedShort-totalDigits-3-NS"

    value: int = field(
        metadata={
            "total_digits": 3,
        }
    )
