from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-negativeInteger-maxExclusive-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicNegativeIntegerMaxExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-negativeInteger-maxExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-negativeInteger-maxExclusive-4-NS"

    value: int = field(
        metadata={
            "max_exclusive": -572450131914860271,
        }
    )
