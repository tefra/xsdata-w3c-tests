from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-date-pattern-4-NS"


@dataclass
class NistschemaSvIvListDatePattern4:
    class Meta:
        name = "NISTSchema-SV-IV-list-date-pattern-4"
        namespace = "NISTSchema-SV-IV-list-date-pattern-4-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "pattern": r"20\d\d-\d0-1\d \d\d75-\d5-2\d \d\d34-0\d-2\d 19\d\d-0\d-\d4 \d\d09-0\d-\d6 19\d\d-\d3-\d2",
            "tokens": True,
        }
    )
