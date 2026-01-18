from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-dateTime-pattern-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListDateTimePattern2:
    class Meta:
        name = "NISTSchema-SV-IV-list-dateTime-pattern-2"
        namespace = "NISTSchema-SV-IV-list-dateTime-pattern-2-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\d\d67-0\d-0\dT1\d:2\d:0\d 18\d\d-\d6-\d8T0\d:\d9:2\d 19\d\d-\d2-\d6T0\d:0\d:\d8 \d\d09-1\d-\d2T1\d:\d7:3\d 19\d\d-\d6-1\dT\d7:5\d:\d1 \d\d43-0\d-\d6T1\d:2\d:\d8 18\d\d-0\d-\d7T\d2:4\d:\d3",
            "tokens": True,
        },
    )
