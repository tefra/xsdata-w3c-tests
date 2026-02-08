from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedByte-maxExclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedByteMaxExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedByte-maxExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-unsignedByte-maxExclusive-3-NS"

    value: int = field(
        metadata={
            "max_exclusive": 10,
        }
    )
