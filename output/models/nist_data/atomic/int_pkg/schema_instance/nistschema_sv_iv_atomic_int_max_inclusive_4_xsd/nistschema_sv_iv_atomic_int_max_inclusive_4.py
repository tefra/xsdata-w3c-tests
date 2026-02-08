from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-int-maxInclusive-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicIntMaxInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-int-maxInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-int-maxInclusive-4-NS"

    value: int = field(
        metadata={
            "max_inclusive": 348085051,
        }
    )
