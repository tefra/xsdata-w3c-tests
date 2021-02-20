from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-dateTime-pattern-5-NS"


@dataclass
class NistschemaSvIvListDateTimePattern5:
    class Meta:
        name = "NISTSchema-SV-IV-list-dateTime-pattern-5"
        namespace = "NISTSchema-SV-IV-list-dateTime-pattern-5-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"\d\d84-0\d-2\dT0\d:\d1:\d1 \d\d85-0\d-0\dT1\d:\d4:2\d 20\d\d-\d1-2\dT\d5:0\d:\d2 \d\d12-0\d-\d7T\d0:3\d:\d2 \d\d82-0\d-\d9T1\d:0\d:\d8",
            "tokens": True,
        }
    )
