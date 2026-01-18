from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-boolean-pattern-1-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListBooleanPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-list-boolean-pattern-1"
        namespace = "NISTSchema-SV-IV-list-boolean-pattern-1-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"true [0]{1} [0]{1} false [1]{1} false",
            "tokens": True,
        },
    )
