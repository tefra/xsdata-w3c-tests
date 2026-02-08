from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedLong-minExclusive-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedLongMinExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedLong-minExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-unsignedLong-minExclusive-4-NS"

    value: int = field(
        metadata={
            "min_exclusive": 595843373185442780,
        }
    )
