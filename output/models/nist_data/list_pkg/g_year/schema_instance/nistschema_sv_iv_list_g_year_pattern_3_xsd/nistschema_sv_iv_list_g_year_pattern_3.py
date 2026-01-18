from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYear-pattern-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListGYearPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-list-gYear-pattern-3"
        namespace = "NISTSchema-SV-IV-list-gYear-pattern-3-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\d\d93 \d\d27 18\d\d \d\d15 19\d\d \d\d57 18\d\d 19\d\d \d\d57",
            "tokens": True,
        },
    )
