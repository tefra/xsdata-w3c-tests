from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonthDay-pattern-5-NS"


@dataclass
class NistschemaSvIvListGMonthDayPattern5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonthDay-pattern-5"
        namespace = "NISTSchema-SV-IV-list-gMonthDay-pattern-5-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            pattern=r"--0\d-1\d --\d3-1\d --0\d-\d3 --\d5-\d7 --\d2-2\d --0\d-0\d --0\d-1\d --\d1-\d9 --0\d-2\d"
        )
    )