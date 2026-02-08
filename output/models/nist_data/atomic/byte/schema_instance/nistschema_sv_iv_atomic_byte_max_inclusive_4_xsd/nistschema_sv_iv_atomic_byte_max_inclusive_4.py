from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-byte-maxInclusive-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicByteMaxInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-byte-maxInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-byte-maxInclusive-4-NS"

    value: int = field(
        metadata={
            "max_inclusive": -47,
        }
    )
