from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-positiveInteger-maxExclusive-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicPositiveIntegerMaxExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-positiveInteger-maxExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-positiveInteger-maxExclusive-4-NS"

    value: int = field(
        metadata={
            "max_exclusive": 571841216500225568,
        }
    )
