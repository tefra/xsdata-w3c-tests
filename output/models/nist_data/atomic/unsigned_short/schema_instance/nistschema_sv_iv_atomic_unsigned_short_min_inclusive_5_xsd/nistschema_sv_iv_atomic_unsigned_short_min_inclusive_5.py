from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedShort-minInclusive-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedShortMinInclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedShort-minInclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-unsignedShort-minInclusive-5-NS"

    value: int = field(
        metadata={
            "min_inclusive": 65535,
        }
    )
