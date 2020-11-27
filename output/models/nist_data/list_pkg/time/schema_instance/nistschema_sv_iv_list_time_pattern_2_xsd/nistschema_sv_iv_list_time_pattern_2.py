from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-time-pattern-2-NS"


@dataclass
class NistschemaSvIvListTimePattern2:
    class Meta:
        name = "NISTSchema-SV-IV-list-time-pattern-2"
        namespace = "NISTSchema-SV-IV-list-time-pattern-2-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "pattern": r"0\d:3\d:\d1 1\d:1\d:1\d \d5:\d6:5\d 0\d:\d2:0\d \d7:4\d:0\d 1\d:2\d:5\d 0\d:\d4:5\d \d6:\d4:1\d",
            "tokens": True,
        }
    )
