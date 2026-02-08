from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-long-maxExclusive-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicLongMaxExclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-long-maxExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-long-maxExclusive-1-NS"

    value: int = field(
        metadata={
            "max_exclusive": -999999999999999998,
        }
    )
