from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedShort-minExclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedShortMinExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedShort-minExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-unsignedShort-minExclusive-3-NS"

    value: int = field(
        metadata={
            "min_exclusive": 42506,
        }
    )
