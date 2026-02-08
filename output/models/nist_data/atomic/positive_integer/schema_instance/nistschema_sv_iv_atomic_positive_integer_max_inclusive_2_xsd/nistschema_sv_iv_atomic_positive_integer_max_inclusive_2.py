from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-positiveInteger-maxInclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicPositiveIntegerMaxInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-positiveInteger-maxInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-positiveInteger-maxInclusive-2-NS"

    value: int = field(
        metadata={
            "max_inclusive": 423285904007674851,
        }
    )
