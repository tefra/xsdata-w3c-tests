from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-dateTime-pattern-3-NS"


@dataclass
class NistschemaSvIvListDateTimePattern3:
    class Meta:
        name = "NISTSchema-SV-IV-list-dateTime-pattern-3"
        namespace = "NISTSchema-SV-IV-list-dateTime-pattern-3-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"17\d\d-\d0-\d1T\d4:1\d:1\d 19\d\d-0\d-0\dT1\d:2\d:4\d \d\d91-0\d-0\dT1\d:3\d:3\d \d\d31-0\d-\d7T\d2:\d4:\d5 20\d\d-\d4-0\dT0\d:\d3:1\d \d\d29-\d7-2\dT1\d:4\d:\d6 \d\d24-\d7-\d5T0\d:4\d:\d1 \d\d38-\d6-\d5T\d7:4\d:\d2 19\d\d-0\d-\d2T0\d:\d9:1\d",
            "tokens": True,
        },
    )
