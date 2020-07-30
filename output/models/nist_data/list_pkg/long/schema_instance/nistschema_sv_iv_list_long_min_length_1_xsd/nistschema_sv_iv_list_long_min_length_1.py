from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-long-minLength-1-NS"


@dataclass
class NistschemaSvIvListLongMinLength1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-long-minLength-1"
        namespace = "NISTSchema-SV-IV-list-long-minLength-1-NS"

    value: List[int] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            min_length=5
        )
    )
