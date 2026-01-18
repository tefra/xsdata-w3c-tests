from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonNegativeInteger-minInclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNonNegativeIntegerMinInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonNegativeInteger-minInclusive-2"
        namespace = (
            "NISTSchema-SV-IV-atomic-nonNegativeInteger-minInclusive-2-NS"
        )

    value: int = field(
        metadata={
            "required": True,
            "min_inclusive": 414410475494371377,
        }
    )
