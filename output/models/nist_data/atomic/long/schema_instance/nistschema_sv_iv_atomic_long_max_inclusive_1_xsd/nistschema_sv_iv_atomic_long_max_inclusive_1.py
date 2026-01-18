from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-long-maxInclusive-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicLongMaxInclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-long-maxInclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-long-maxInclusive-1-NS"

    value: int = field(
        metadata={
            "required": True,
            "max_inclusive": -999999999999999999,
        }
    )
