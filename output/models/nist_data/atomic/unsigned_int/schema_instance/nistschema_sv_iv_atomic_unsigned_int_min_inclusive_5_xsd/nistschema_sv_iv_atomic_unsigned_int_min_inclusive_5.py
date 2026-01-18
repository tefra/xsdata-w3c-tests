from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-minInclusive-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedIntMinInclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedInt-minInclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-unsignedInt-minInclusive-5-NS"

    value: int = field(
        metadata={
            "required": True,
            "min_inclusive": 4294967295,
        }
    )
