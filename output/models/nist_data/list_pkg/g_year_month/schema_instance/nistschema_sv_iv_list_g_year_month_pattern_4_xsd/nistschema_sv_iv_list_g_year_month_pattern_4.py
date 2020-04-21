from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYearMonth-pattern-4-NS"


@dataclass
class NistschemaSvIvListGYearMonthPattern4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-gYearMonth-pattern-4"
        namespace = "NISTSchema-SV-IV-list-gYearMonth-pattern-4-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            pattern=r"\d\d93-\d3 19\d\d-0\d \d\d33-\d3 18\d\d-\d1 \d\d34-0\d"
        )
    )
