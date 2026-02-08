from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedShort-maxExclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicUnsignedShortMaxExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedShort-maxExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-unsignedShort-maxExclusive-2-NS"

    value: int = field(
        metadata={
            "max_exclusive": 8410,
        }
    )
