from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonth-pattern-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGMonthPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonth-pattern-5"
        namespace = "NISTSchema-SV-IV-atomic-gMonth-pattern-5-NS"

    value: str = field(
        default="",
        metadata={
            "pattern": r"--0\d",
        },
    )
