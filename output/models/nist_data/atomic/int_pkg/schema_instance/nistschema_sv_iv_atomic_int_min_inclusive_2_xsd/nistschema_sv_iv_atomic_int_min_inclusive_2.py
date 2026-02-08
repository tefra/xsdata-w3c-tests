from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-int-minInclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicIntMinInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-int-minInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-int-minInclusive-2-NS"

    value: int = field(
        metadata={
            "min_inclusive": -1728117668,
        }
    )
