from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-integer-minInclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicIntegerMinInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-integer-minInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-integer-minInclusive-3-NS"

    value: int = field(
        metadata={
            "min_inclusive": -362471093580558400,
        }
    )
