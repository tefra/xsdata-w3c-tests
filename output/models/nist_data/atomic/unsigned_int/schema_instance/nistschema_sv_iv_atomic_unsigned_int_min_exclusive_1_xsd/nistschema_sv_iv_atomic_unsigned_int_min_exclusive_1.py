from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-minExclusive-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedIntMinExclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedInt-minExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-unsignedInt-minExclusive-1-NS"

    value: int = field(
        metadata={
            "min_exclusive": 0,
        }
    )
