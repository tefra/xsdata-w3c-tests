from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-maxInclusive-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedIntMaxInclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedInt-maxInclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-unsignedInt-maxInclusive-5-NS"

    value: int = field(
        metadata={
            "max_inclusive": 4294967295,
        }
    )
