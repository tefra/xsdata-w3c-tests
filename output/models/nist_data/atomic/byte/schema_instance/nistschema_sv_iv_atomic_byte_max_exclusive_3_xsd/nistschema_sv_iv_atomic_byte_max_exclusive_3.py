from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-byte-maxExclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicByteMaxExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-byte-maxExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-byte-maxExclusive-3-NS"

    value: int = field(
        metadata={
            "max_exclusive": 103,
        }
    )
