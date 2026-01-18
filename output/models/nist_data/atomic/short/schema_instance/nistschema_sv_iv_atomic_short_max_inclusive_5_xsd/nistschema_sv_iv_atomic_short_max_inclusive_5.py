from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-short-maxInclusive-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicShortMaxInclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-short-maxInclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-short-maxInclusive-5-NS"

    value: int = field(
        metadata={
            "required": True,
            "max_inclusive": 32767,
        }
    )
