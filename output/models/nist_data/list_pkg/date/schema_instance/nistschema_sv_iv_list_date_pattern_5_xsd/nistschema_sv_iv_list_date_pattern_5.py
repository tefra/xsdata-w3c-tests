from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-date-pattern-5-NS"


@dataclass
class NistschemaSvIvListDatePattern5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-date-pattern-5"
        namespace = "NISTSchema-SV-IV-list-date-pattern-5-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            pattern=r"\d\d74-\d7-\d5 17\d\d-0\d-2\d 19\d\d-\d1-\d8 \d\d25-\d2-1\d 19\d\d-\d8-\d5"
        )
    )