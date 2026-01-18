from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedByte-totalDigits-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedByteTotalDigits1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedByte-totalDigits-1"
        namespace = "NISTSchema-SV-IV-atomic-unsignedByte-totalDigits-1-NS"

    value: int = field(
        metadata={
            "required": True,
            "total_digits": 1,
        }
    )
