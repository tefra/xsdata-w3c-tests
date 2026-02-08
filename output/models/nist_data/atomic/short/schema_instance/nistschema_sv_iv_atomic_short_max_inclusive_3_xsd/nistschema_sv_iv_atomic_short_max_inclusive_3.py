from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-short-maxInclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicShortMaxInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-short-maxInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-short-maxInclusive-3-NS"

    value: int = field(
        metadata={
            "max_inclusive": -25835,
        }
    )
