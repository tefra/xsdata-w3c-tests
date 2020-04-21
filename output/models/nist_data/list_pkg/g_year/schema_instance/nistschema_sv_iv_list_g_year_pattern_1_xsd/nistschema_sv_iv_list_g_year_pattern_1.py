from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYear-pattern-1-NS"


@dataclass
class NistschemaSvIvListGYearPattern1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-gYear-pattern-1"
        namespace = "NISTSchema-SV-IV-list-gYear-pattern-1-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            pattern=r"\d\d81 \d\d41 18\d\d \d\d64 19\d\d \d\d72 \d\d38 \d\d27"
        )
    )
