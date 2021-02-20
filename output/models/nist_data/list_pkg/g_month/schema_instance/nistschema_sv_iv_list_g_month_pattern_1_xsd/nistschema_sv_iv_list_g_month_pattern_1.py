from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonth-pattern-1-NS"


@dataclass
class NistschemaSvIvListGMonthPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonth-pattern-1"
        namespace = "NISTSchema-SV-IV-list-gMonth-pattern-1-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"--\d9 --\d4 --\d0 --0\d --\d3 --\d8 --0\d --\d1",
            "tokens": True,
        }
    )
