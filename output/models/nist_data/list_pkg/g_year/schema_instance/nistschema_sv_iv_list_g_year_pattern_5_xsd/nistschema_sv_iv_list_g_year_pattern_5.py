from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYear-pattern-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListGYearPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-list-gYear-pattern-5"
        namespace = "NISTSchema-SV-IV-list-gYear-pattern-5-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"18\d\d \d\d52 \d\d14 20\d\d \d\d14 \d\d43 \d\d70 19\d\d \d\d36",
            "tokens": True,
        },
    )
