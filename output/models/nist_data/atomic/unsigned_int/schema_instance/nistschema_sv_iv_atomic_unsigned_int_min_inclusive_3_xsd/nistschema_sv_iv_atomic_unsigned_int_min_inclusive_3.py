from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-minInclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedIntMinInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedInt-minInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-unsignedInt-minInclusive-3-NS"

    value: int = field(
        metadata={
            "required": True,
            "min_inclusive": 2401546713,
        }
    )
