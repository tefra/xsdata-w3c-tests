from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedShort-maxInclusive-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedShortMaxInclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedShort-maxInclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-unsignedShort-maxInclusive-5-NS"

    value: int = field(
        metadata={
            "required": True,
            "max_inclusive": 65535,
        }
    )
