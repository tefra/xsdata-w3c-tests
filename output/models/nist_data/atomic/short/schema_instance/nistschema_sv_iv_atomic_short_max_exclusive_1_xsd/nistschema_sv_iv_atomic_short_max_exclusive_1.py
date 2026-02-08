from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-short-maxExclusive-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicShortMaxExclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-short-maxExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-short-maxExclusive-1-NS"

    value: int = field(
        metadata={
            "max_exclusive": -32767,
        }
    )
