from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-minInclusive-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedIntMinInclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedInt-minInclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-unsignedInt-minInclusive-1-NS"

    value: int = field(
        metadata={
            "min_inclusive": 0,
        }
    )
