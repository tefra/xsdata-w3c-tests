from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-time-pattern-5-NS"


@dataclass
class NistschemaSvIvListTimePattern5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-time-pattern-5"
        namespace = "NISTSchema-SV-IV-list-time-pattern-5-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            pattern=r"\d2:\d8:3\d 1\d:\d7:\d5 1\d:\d4:0\d \d3:\d9:4\d \d4:4\d:3\d"
        )
    )