from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYearMonth-pattern-3-NS"


@dataclass
class NistschemaSvIvListGYearMonthPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-list-gYearMonth-pattern-3"
        namespace = "NISTSchema-SV-IV-list-gYearMonth-pattern-3-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\d\d74-0\d 18\d\d-\d8 \d\d80-1\d 20\d\d-\d2 \d\d08-0\d 19\d\d-0\d \d\d12-\d1 \d\d25-\d6 \d\d19-0\d",
            "tokens": True,
        }
    )
