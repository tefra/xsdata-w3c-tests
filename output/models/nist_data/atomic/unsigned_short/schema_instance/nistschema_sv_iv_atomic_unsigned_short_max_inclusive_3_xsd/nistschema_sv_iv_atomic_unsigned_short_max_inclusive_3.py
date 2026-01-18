from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedShort-maxInclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedShortMaxInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedShort-maxInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-unsignedShort-maxInclusive-3-NS"

    value: int = field(
        metadata={
            "required": True,
            "max_inclusive": 21008,
        }
    )
