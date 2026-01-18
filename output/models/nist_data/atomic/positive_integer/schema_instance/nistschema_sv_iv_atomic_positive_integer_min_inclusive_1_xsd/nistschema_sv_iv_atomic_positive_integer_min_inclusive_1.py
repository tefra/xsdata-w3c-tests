from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-positiveInteger-minInclusive-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicPositiveIntegerMinInclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-positiveInteger-minInclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-positiveInteger-minInclusive-1-NS"

    value: int = field(
        metadata={
            "required": True,
            "min_inclusive": 1,
        }
    )
