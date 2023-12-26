from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYearMonth-pattern-5-NS"


@dataclass
class NistschemaSvIvListGYearMonthPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-list-gYearMonth-pattern-5"
        namespace = "NISTSchema-SV-IV-list-gYearMonth-pattern-5-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"19\d\d-1\d \d\d06-\d9 17\d\d-0\d \d\d20-\d1 \d\d77-0\d \d\d19-\d3 17\d\d-1\d",
            "tokens": True,
        },
    )
