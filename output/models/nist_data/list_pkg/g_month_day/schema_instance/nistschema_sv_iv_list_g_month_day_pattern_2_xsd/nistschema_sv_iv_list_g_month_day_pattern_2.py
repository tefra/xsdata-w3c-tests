from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonthDay-pattern-2-NS"


@dataclass
class NistschemaSvIvListGMonthDayPattern2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonthDay-pattern-2"
        namespace = "NISTSchema-SV-IV-list-gMonthDay-pattern-2-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            pattern=r"--\d5-\d2 --\d4-\d4 --0\d-\d3 --\d7-\d6 --\d5-0\d --0\d-0\d --0\d-1\d --\d8-\d6 --0\d-\d9",
            tokens=True
        )
    )
