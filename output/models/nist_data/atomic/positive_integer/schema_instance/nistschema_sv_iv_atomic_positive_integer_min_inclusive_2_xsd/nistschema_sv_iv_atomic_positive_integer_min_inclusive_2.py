from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-positiveInteger-minInclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicPositiveIntegerMinInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-positiveInteger-minInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-positiveInteger-minInclusive-2-NS"

    value: int = field(
        metadata={
            "min_inclusive": 15066261577183049,
        }
    )
