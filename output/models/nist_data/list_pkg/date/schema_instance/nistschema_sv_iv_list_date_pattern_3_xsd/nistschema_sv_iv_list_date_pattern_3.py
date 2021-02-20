from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-date-pattern-3-NS"


@dataclass
class NistschemaSvIvListDatePattern3:
    class Meta:
        name = "NISTSchema-SV-IV-list-date-pattern-3"
        namespace = "NISTSchema-SV-IV-list-date-pattern-3-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\d\d47-0\d-\d2 18\d\d-0\d-\d5 20\d\d-1\d-2\d \d\d79-0\d-1\d \d\d70-\d0-0\d 18\d\d-\d6-0\d \d\d22-0\d-\d1",
            "tokens": True,
        }
    )
