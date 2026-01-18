from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-int-maxExclusive-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicIntMaxExclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-int-maxExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-int-maxExclusive-5-NS"

    value: int = field(
        metadata={
            "required": True,
            "max_exclusive": 2147483647,
        }
    )
