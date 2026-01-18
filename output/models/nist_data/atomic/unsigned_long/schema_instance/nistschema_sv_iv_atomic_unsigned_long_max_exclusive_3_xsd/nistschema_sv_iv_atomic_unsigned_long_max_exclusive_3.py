from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedLong-maxExclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedLongMaxExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedLong-maxExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-unsignedLong-maxExclusive-3-NS"

    value: int = field(
        metadata={
            "required": True,
            "max_exclusive": 114762413382550444,
        }
    )
