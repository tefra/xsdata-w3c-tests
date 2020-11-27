from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-pattern-2-NS"


@dataclass
class NistschemaSvIvUnionGMonthDayGYearMonthPattern2:
    class Meta:
        name = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-pattern-2"
        namespace = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-pattern-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"\d\d65-\d1",
        }
    )
