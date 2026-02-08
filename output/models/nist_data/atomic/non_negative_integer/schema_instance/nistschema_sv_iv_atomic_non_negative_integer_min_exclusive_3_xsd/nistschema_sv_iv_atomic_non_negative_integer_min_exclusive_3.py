from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonNegativeInteger-minExclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNonNegativeIntegerMinExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonNegativeInteger-minExclusive-3"
        namespace = (
            "NISTSchema-SV-IV-atomic-nonNegativeInteger-minExclusive-3-NS"
        )

    value: int = field(
        metadata={
            "min_exclusive": 12032691129748584,
        }
    )
