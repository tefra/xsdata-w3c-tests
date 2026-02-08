from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-minExclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedIntMinExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedInt-minExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-unsignedInt-minExclusive-2-NS"

    value: int = field(
        metadata={
            "min_exclusive": 72170852,
        }
    )
