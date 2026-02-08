from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-maxExclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedIntMaxExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedInt-maxExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-unsignedInt-maxExclusive-3-NS"

    value: int = field(
        metadata={
            "max_exclusive": 1539442072,
        }
    )
