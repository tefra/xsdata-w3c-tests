from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-long-maxExclusive-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicLongMaxExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-long-maxExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-long-maxExclusive-4-NS"

    value: int = field(
        metadata={
            "max_exclusive": -40900034799576711,
        }
    )
