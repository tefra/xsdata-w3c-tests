from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonPositiveInteger-minInclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNonPositiveIntegerMinInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonPositiveInteger-minInclusive-2"
        namespace = (
            "NISTSchema-SV-IV-atomic-nonPositiveInteger-minInclusive-2-NS"
        )

    value: int = field(
        metadata={
            "required": True,
            "min_inclusive": -927820889571802863,
        }
    )
