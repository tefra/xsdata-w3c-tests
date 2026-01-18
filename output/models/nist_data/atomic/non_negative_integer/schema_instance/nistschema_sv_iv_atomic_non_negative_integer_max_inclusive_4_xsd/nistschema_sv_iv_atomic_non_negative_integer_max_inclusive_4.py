from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonNegativeInteger-maxInclusive-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNonNegativeIntegerMaxInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonNegativeInteger-maxInclusive-4"
        namespace = (
            "NISTSchema-SV-IV-atomic-nonNegativeInteger-maxInclusive-4-NS"
        )

    value: int = field(
        metadata={
            "required": True,
            "max_inclusive": 467117575036009479,
        }
    )
