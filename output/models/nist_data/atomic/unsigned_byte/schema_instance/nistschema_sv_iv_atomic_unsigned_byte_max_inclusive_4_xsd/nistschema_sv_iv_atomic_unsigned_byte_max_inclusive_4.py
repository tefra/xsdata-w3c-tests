from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedByte-maxInclusive-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedByteMaxInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedByte-maxInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-unsignedByte-maxInclusive-4-NS"

    value: int = field(
        metadata={
            "max_inclusive": 217,
        }
    )
