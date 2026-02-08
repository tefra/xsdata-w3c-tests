from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-integer-minExclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicIntegerMinExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-integer-minExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-integer-minExclusive-3-NS"

    value: int = field(
        metadata={
            "min_exclusive": 389578809107570477,
        }
    )
