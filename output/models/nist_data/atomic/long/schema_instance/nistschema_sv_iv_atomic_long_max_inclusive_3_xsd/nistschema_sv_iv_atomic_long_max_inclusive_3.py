from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-long-maxInclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicLongMaxInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-long-maxInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-long-maxInclusive-3-NS"

    value: int = field(
        metadata={
            "max_inclusive": -319274017545440269,
        }
    )
