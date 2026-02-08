from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-integer-minInclusive-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicIntegerMinInclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-integer-minInclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-integer-minInclusive-1-NS"

    value: int = field(
        metadata={
            "min_inclusive": -999999999999999999,
        }
    )
