from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-positiveInteger-minInclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicPositiveIntegerMinInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-positiveInteger-minInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-positiveInteger-minInclusive-3-NS"

    value: int = field(
        metadata={
            "required": True,
            "min_inclusive": 828758841369869991,
        }
    )
