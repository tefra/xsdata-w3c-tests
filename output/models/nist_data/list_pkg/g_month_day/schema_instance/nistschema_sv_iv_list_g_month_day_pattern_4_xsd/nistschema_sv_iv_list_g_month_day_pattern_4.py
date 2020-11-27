from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonthDay-pattern-4-NS"


@dataclass
class NistschemaSvIvListGMonthDayPattern4:
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonthDay-pattern-4"
        namespace = "NISTSchema-SV-IV-list-gMonthDay-pattern-4-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "pattern": r"--\d7-\d5 --0\d-\d2 --0\d-2\d --0\d-\d3 --\d1-\d0 --0\d-\d6 --\d6-0\d --1\d-1\d --\d1-2\d",
            "tokens": True,
        }
    )
