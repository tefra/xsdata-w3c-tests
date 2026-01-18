from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonNegativeInteger-minInclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNonNegativeIntegerMinInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonNegativeInteger-minInclusive-3"
        namespace = (
            "NISTSchema-SV-IV-atomic-nonNegativeInteger-minInclusive-3-NS"
        )

    value: int = field(
        metadata={
            "required": True,
            "min_inclusive": 543609894158592842,
        }
    )
