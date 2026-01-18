from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-byte-maxInclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicByteMaxInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-byte-maxInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-byte-maxInclusive-3-NS"

    value: int = field(
        metadata={
            "required": True,
            "max_inclusive": 17,
        }
    )
