from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-pattern-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvAtomicGYearMonthPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-pattern-1"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-pattern-1-NS"

    value: str = field(
        default="",
        metadata={
            "pattern": r"17\d\d-\d1",
        },
    )
