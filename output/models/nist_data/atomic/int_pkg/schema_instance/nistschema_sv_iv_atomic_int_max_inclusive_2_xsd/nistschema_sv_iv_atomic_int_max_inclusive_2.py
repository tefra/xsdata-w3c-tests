from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-int-maxInclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicIntMaxInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-int-maxInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-int-maxInclusive-2-NS"

    value: int = field(
        metadata={
            "required": True,
            "max_inclusive": -1910754291,
        }
    )
