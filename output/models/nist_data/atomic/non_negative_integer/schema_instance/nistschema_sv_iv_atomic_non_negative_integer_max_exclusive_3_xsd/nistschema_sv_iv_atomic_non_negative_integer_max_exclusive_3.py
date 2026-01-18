from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonNegativeInteger-maxExclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNonNegativeIntegerMaxExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonNegativeInteger-maxExclusive-3"
        namespace = (
            "NISTSchema-SV-IV-atomic-nonNegativeInteger-maxExclusive-3-NS"
        )

    value: int = field(
        metadata={
            "required": True,
            "max_exclusive": 278524439385076983,
        }
    )
