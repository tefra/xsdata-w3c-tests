from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-long-maxExclusive-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicLongMaxExclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-long-maxExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-long-maxExclusive-5-NS"

    value: int = field(
        metadata={
            "required": True,
            "max_exclusive": 999999999999999999,
        }
    )
