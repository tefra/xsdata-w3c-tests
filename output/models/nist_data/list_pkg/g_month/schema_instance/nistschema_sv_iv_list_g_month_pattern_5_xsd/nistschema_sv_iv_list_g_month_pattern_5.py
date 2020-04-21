from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-gMonth-pattern-5-NS"


@dataclass
class NistschemaSvIvListGMonthPattern5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-gMonth-pattern-5"
        namespace = "NISTSchema-SV-IV-list-gMonth-pattern-5-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            pattern=r"--1\d --0\d --1\d --\d8 --\d8 --\d7 --0\d --\d8"
        )
    )
