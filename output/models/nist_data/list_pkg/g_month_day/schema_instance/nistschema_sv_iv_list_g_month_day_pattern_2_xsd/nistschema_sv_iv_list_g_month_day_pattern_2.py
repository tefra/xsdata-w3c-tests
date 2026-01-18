from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonthDay-pattern-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListGMonthDayPattern2:
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonthDay-pattern-2"
        namespace = "NISTSchema-SV-IV-list-gMonthDay-pattern-2-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"--\d5-\d2 --\d4-\d4 --0\d-\d3 --\d7-\d6 --\d5-0\d --0\d-0\d --0\d-1\d --\d8-\d6 --0\d-\d9",
            "tokens": True,
        },
    )
