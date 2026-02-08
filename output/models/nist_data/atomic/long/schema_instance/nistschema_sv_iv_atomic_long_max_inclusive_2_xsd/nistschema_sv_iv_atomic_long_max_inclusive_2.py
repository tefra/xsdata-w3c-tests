from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-long-maxInclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicLongMaxInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-long-maxInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-long-maxInclusive-2-NS"

    value: int = field(
        metadata={
            "max_inclusive": 472512421492236489,
        }
    )
