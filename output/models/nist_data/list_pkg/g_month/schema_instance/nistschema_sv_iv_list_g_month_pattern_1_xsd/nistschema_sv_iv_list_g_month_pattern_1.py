from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonth-pattern-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListGMonthPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonth-pattern-1"
        namespace = "NISTSchema-SV-IV-list-gMonth-pattern-1-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"--\d9 --\d4 --\d0 --0\d --\d3 --\d8 --0\d --\d1",
            "tokens": True,
        },
    )
