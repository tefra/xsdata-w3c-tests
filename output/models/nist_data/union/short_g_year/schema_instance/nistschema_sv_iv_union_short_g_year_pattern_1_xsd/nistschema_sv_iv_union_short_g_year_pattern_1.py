from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-union-short-gYear-pattern-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvUnionShortGYearPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-union-short-gYear-pattern-1"
        namespace = "NISTSchema-SV-IV-union-short-gYear-pattern-1-NS"

    value: str = field(
        default="",
        metadata={
            "pattern": r"\d\d70",
        },
    )
