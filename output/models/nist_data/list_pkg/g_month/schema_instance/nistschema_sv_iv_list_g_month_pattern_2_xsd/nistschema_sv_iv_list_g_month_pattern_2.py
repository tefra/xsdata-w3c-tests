from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonth-pattern-2-NS"


@dataclass
class NistschemaSvIvListGMonthPattern2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonth-pattern-2"
        namespace = "NISTSchema-SV-IV-list-gMonth-pattern-2-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            pattern=r"--1\d --1\d --1\d --1\d --0\d --\d3",
            tokens=True
        )
    )
