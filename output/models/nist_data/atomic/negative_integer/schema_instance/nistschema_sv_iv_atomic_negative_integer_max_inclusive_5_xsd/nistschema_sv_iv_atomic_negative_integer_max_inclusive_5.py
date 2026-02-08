from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-negativeInteger-maxInclusive-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNegativeIntegerMaxInclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-negativeInteger-maxInclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-negativeInteger-maxInclusive-5-NS"

    value: int = field(
        metadata={
            "max_inclusive": -1,
        }
    )
