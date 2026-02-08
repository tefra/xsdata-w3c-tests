from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-long-maxExclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicLongMaxExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-long-maxExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-long-maxExclusive-3-NS"

    value: int = field(
        metadata={
            "max_exclusive": -62970516107334394,
        }
    )
