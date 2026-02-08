from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-negativeInteger-minInclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNegativeIntegerMinInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-negativeInteger-minInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-negativeInteger-minInclusive-3-NS"

    value: int = field(
        metadata={
            "min_inclusive": -539945622984702833,
        }
    )
