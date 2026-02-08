from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-minExclusive-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedIntMinExclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedInt-minExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-unsignedInt-minExclusive-5-NS"

    value: int = field(
        metadata={
            "min_exclusive": 4294967294,
        }
    )
