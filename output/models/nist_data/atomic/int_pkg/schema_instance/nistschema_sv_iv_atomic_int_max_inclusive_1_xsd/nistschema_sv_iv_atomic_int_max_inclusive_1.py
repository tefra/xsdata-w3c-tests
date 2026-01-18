from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-int-maxInclusive-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicIntMaxInclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-int-maxInclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-int-maxInclusive-1-NS"

    value: int = field(
        metadata={
            "required": True,
            "max_inclusive": -2147483648,
        }
    )
