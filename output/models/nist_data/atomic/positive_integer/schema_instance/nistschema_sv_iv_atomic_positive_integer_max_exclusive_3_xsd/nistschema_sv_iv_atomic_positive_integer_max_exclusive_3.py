from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-positiveInteger-maxExclusive-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicPositiveIntegerMaxExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-positiveInteger-maxExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-positiveInteger-maxExclusive-3-NS"

    value: int = field(
        metadata={
            "max_exclusive": 685616415831176051,
        }
    )
