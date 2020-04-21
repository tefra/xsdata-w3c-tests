from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-date-pattern-2-NS"


@dataclass
class NistschemaSvIvListDatePattern2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-date-pattern-2"
        namespace = "NISTSchema-SV-IV-list-date-pattern-2-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            pattern=r"\d\d56-\d1-0\d \d\d57-0\d-2\d \d\d49-1\d-\d4 18\d\d-\d3-2\d 19\d\d-\d7-\d7 19\d\d-1\d-0\d"
        )
    )
