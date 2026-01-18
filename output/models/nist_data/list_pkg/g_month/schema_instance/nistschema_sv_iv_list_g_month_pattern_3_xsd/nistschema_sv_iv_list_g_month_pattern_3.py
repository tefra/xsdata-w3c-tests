from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonth-pattern-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListGMonthPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonth-pattern-3"
        namespace = "NISTSchema-SV-IV-list-gMonth-pattern-3-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"--1\d --0\d --1\d --0\d --0\d --0\d --\d8",
            "tokens": True,
        },
    )
