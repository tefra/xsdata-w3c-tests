from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYearMonth-pattern-1-NS"


@dataclass
class NistschemaSvIvListGYearMonthPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-list-gYearMonth-pattern-1"
        namespace = "NISTSchema-SV-IV-list-gYearMonth-pattern-1-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"18\d\d-0\d \d\d92-\d2 \d\d99-0\d \d\d49-\d4 19\d\d-\d1 \d\d74-0\d 18\d\d-\d5 19\d\d-1\d \d\d68-0\d",
            "tokens": True,
        },
    )
