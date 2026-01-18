from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-maxExclusive-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedIntMaxExclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedInt-maxExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-unsignedInt-maxExclusive-5-NS"

    value: int = field(
        metadata={
            "required": True,
            "max_exclusive": 4294967295,
        }
    )
