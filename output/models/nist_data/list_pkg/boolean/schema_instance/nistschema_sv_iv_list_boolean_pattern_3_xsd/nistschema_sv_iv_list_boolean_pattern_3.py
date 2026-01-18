from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-boolean-pattern-3-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListBooleanPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-list-boolean-pattern-3"
        namespace = "NISTSchema-SV-IV-list-boolean-pattern-3-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"[1]{1} false [1]{1} true [1]{1}",
            "tokens": True,
        },
    )
