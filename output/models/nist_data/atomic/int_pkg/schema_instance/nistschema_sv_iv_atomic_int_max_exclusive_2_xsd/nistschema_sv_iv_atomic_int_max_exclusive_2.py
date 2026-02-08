from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-int-maxExclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicIntMaxExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-int-maxExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-int-maxExclusive-2-NS"

    value: int = field(
        metadata={
            "max_exclusive": -1810120723,
        }
    )
