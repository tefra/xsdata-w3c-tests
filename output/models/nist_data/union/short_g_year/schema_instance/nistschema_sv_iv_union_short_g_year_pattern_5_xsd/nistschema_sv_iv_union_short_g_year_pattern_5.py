from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-union-short-gYear-pattern-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvUnionShortGYearPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-union-short-gYear-pattern-5"
        namespace = "NISTSchema-SV-IV-union-short-gYear-pattern-5-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"\d{5}",
        },
    )
