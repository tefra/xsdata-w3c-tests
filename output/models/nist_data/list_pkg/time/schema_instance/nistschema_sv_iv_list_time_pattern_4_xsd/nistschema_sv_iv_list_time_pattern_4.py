from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-time-pattern-4-NS"


@dataclass
class NistschemaSvIvListTimePattern4:
    class Meta:
        name = "NISTSchema-SV-IV-list-time-pattern-4"
        namespace = "NISTSchema-SV-IV-list-time-pattern-4-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\d8:0\d:0\d 0\d:2\d:2\d \d0:\d8:2\d 0\d:0\d:\d6 \d1:\d0:\d5",
            "tokens": True,
        }
    )
