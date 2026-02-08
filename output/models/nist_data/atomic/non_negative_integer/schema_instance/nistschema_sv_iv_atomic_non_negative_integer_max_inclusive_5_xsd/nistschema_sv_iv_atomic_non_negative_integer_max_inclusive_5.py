from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonNegativeInteger-maxInclusive-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNonNegativeIntegerMaxInclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonNegativeInteger-maxInclusive-5"
        namespace = (
            "NISTSchema-SV-IV-atomic-nonNegativeInteger-maxInclusive-5-NS"
        )

    value: int = field(
        metadata={
            "max_inclusive": 999999999999999999,
        }
    )
