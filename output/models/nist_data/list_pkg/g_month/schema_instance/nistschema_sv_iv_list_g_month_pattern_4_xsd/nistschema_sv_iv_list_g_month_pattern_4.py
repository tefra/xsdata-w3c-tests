from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonth-pattern-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListGMonthPattern4:
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonth-pattern-4"
        namespace = "NISTSchema-SV-IV-list-gMonth-pattern-4-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"--\d1 --\d0 --\d1 --0\d --\d9 --\d2 --\d1 --\d3 --1\d",
            "tokens": True,
        },
    )
