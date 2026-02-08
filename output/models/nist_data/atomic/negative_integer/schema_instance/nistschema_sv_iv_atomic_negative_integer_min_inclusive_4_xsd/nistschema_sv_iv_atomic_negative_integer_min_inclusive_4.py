from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-negativeInteger-minInclusive-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNegativeIntegerMinInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-negativeInteger-minInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-negativeInteger-minInclusive-4-NS"

    value: int = field(
        metadata={
            "min_inclusive": -947674826094804355,
        }
    )
