from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-int-maxInclusive-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicIntMaxInclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-int-maxInclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-int-maxInclusive-5-NS"

    value: int = field(
        metadata={
            "required": True,
            "max_inclusive": 2147483647,
        }
    )
