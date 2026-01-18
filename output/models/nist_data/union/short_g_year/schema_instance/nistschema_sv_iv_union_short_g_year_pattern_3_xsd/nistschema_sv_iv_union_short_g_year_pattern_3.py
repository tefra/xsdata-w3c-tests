from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-union-short-gYear-pattern-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvUnionShortGYearPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-union-short-gYear-pattern-3"
        namespace = "NISTSchema-SV-IV-union-short-gYear-pattern-3-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\d\d50",
        },
    )
