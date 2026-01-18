from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-list-gDay-pattern-2-NS"


@dataclass(kw_only=True)
class NistschemaSvIvListGDayPattern2:
    class Meta:
        name = "NISTSchema-SV-IV-list-gDay-pattern-2"
        namespace = "NISTSchema-SV-IV-list-gDay-pattern-2-NS"

    value: list[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"---1\d ---\d4 ---1\d ---\d2 ---\d8 ---\d9 ---1\d ---\d1 ---\d4",
            "tokens": True,
        },
    )
