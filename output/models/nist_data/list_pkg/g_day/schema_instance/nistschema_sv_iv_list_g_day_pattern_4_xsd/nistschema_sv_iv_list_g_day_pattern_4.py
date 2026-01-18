from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-gDay-pattern-4-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListGDayPattern4:
    class Meta:
        name = "NISTSchema-SV-IV-list-gDay-pattern-4"
        namespace = "NISTSchema-SV-IV-list-gDay-pattern-4-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"---1\d ---2\d ---\d7 ---2\d ---\d6",
            "tokens": True,
        },
    )
