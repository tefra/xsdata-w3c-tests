from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-boolean-pattern-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListBooleanPattern4:
    class Meta:
        name = "NISTSchema-SV-IV-list-boolean-pattern-4"
        namespace = "NISTSchema-SV-IV-list-boolean-pattern-4-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"[1]{1} false [0]{1} true true [0]{1}",
            "tokens": True,
        },
    )
