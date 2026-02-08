from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-short-maxInclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicShortMaxInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-short-maxInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-short-maxInclusive-2-NS"

    value: int = field(
        metadata={
            "max_inclusive": 2249,
        }
    )
