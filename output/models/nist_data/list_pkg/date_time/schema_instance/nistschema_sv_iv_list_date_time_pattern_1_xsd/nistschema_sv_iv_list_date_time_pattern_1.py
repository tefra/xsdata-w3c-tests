from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-dateTime-pattern-1-NS"


@dataclass
class NistschemaSvIvListDateTimePattern1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-dateTime-pattern-1"
        namespace = "NISTSchema-SV-IV-list-dateTime-pattern-1-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            pattern=r"\d\d38-\d2-\d5T\d7:\d4:3\d \d\d33-\d5-1\dT\d6:5\d:1\d 18\d\d-\d6-1\dT\d1:\d2:0\d 18\d\d-\d5-1\dT\d4:0\d:5\d \d\d31-\d1-0\dT\d6:5\d:\d9 \d\d49-0\d-1\dT0\d:\d9:4\d \d\d67-0\d-0\dT0\d:\d5:\d9",
            tokens=True
        )
    )
