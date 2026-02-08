from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedLong-minInclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedLongMinInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedLong-minInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-unsignedLong-minInclusive-3-NS"

    value: int = field(
        metadata={
            "min_inclusive": 842438235652469335,
        }
    )
