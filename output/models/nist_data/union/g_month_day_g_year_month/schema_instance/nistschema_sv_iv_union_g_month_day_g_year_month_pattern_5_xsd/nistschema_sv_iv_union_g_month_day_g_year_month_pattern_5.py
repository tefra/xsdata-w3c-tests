from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-pattern-5-NS"


@dataclass(kw_only=True)
class NistschemaSvIvUnionGMonthDayGYearMonthPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-pattern-5"
        namespace = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-pattern-5-NS"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"19\d\d-\d9",
        },
    )
