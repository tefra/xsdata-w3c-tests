from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-time-pattern-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListTimePattern4:
    class Meta:
        name = "NISTSchema-SV-IV-list-time-pattern-4"
        namespace = "NISTSchema-SV-IV-list-time-pattern-4-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\d8:0\d:0\d 0\d:2\d:2\d \d0:\d8:2\d 0\d:0\d:\d6 \d1:\d0:\d5",
            "tokens": True,
        },
    )
