from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-short-pattern-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListShortPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-list-short-pattern-1"
        namespace = "NISTSchema-SV-IV-list-short-pattern-1-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\-\d{5} \-\d{4} \-\d{3} \-\d{2} \-\d{1} \d{5}",
            "tokens": True,
        },
    )
