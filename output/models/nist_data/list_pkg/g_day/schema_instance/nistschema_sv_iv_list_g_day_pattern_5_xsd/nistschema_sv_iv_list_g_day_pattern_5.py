from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-gDay-pattern-5-NS"


@dataclass
class NistschemaSvIvListGDayPattern5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-gDay-pattern-5"
        namespace = "NISTSchema-SV-IV-list-gDay-pattern-5-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            pattern=r"---\d5 ---1\d ---1\d ---0\d ---1\d ---\d9 ---\d3 ---1\d ---\d1 ---1\d"
        )
    )
