from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-dateTime-pattern-4-NS"


@dataclass
class NistschemaSvIvListDateTimePattern4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-dateTime-pattern-4"
        namespace = "NISTSchema-SV-IV-list-dateTime-pattern-4-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            pattern=r"18\d\d-\d7-\d4T\d5:4\d:4\d 20\d\d-\d1-\d0T1\d:\d2:3\d 19\d\d-\d0-\d2T\d2:1\d:\d8 \d\d48-\d5-\d0T\d9:\d4:3\d 17\d\d-\d5-0\dT0\d:\d5:3\d \d\d68-1\d-1\dT\d2:1\d:4\d",
            tokens=True
        )
    )
