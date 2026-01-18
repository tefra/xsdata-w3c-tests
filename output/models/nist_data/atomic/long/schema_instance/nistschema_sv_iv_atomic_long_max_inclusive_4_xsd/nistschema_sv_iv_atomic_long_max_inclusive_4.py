from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-long-maxInclusive-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicLongMaxInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-long-maxInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-long-maxInclusive-4-NS"

    value: int = field(
        metadata={
            "required": True,
            "max_inclusive": 395309234845914847,
        }
    )
