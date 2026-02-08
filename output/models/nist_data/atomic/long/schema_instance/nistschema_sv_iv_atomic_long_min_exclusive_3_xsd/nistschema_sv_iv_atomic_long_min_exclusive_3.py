from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-long-minExclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicLongMinExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-long-minExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-long-minExclusive-3-NS"

    value: int = field(
        metadata={
            "min_exclusive": 420715981815711347,
        }
    )
