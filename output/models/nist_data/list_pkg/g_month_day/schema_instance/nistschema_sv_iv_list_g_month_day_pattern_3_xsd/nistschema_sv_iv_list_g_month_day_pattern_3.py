from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonthDay-pattern-3-NS"


@dataclass
class NistschemaSvIvListGMonthDayPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonthDay-pattern-3"
        namespace = "NISTSchema-SV-IV-list-gMonthDay-pattern-3-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "pattern": r"--\d5-1\d --\d3-2\d --\d4-2\d --0\d-\d2 --\d1-\d3 --\d7-0\d --1\d-\d9 --\d3-0\d",
            "tokens": True,
        }
    )
