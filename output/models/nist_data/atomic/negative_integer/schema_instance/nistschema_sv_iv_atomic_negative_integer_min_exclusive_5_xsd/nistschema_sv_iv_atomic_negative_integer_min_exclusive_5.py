from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-negativeInteger-minExclusive-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNegativeIntegerMinExclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-negativeInteger-minExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-negativeInteger-minExclusive-5-NS"

    value: int = field(
        metadata={
            "min_exclusive": -2,
        }
    )
