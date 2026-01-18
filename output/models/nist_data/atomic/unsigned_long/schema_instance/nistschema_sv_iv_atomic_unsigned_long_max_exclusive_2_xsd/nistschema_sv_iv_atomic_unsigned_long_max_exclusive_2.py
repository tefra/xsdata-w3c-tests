from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedLong-maxExclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedLongMaxExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedLong-maxExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-unsignedLong-maxExclusive-2-NS"

    value: int = field(
        metadata={
            "required": True,
            "max_exclusive": 621144438259934594,
        }
    )
