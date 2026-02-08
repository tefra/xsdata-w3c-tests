from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonNegativeInteger-maxInclusive-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNonNegativeIntegerMaxInclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonNegativeInteger-maxInclusive-1"
        namespace = (
            "NISTSchema-SV-IV-atomic-nonNegativeInteger-maxInclusive-1-NS"
        )

    value: int = field(
        metadata={
            "max_inclusive": 0,
        }
    )
