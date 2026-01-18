from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-int-minInclusive-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicIntMinInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-int-minInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-int-minInclusive-4-NS"

    value: int = field(
        metadata={
            "required": True,
            "min_inclusive": 1012081748,
        }
    )
