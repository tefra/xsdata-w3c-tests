from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-int-minInclusive-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicIntMinInclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-int-minInclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-int-minInclusive-5-NS"

    value: int = field(
        metadata={
            "required": True,
            "min_inclusive": 2147483647,
        }
    )
