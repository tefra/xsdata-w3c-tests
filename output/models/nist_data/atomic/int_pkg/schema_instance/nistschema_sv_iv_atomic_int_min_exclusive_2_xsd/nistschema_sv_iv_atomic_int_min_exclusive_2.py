from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-int-minExclusive-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicIntMinExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-int-minExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-int-minExclusive-2-NS"

    value: int = field(
        metadata={
            "required": True,
            "min_exclusive": -1627498592,
        }
    )
