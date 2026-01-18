from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-negativeInteger-maxInclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNegativeIntegerMaxInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-negativeInteger-maxInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-negativeInteger-maxInclusive-2-NS"

    value: int = field(
        metadata={
            "required": True,
            "max_inclusive": -922333322214573646,
        }
    )
