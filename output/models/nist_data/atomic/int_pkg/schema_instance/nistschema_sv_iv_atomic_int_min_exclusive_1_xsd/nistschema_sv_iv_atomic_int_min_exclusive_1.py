from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-int-minExclusive-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicIntMinExclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-int-minExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-int-minExclusive-1-NS"

    value: int = field(
        metadata={
            "required": True,
            "min_exclusive": -2147483648,
        }
    )
