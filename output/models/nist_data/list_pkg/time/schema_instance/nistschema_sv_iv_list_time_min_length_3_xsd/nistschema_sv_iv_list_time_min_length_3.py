from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-time-minLength-3-NS"


@dataclass
class NistschemaSvIvListTimeMinLength3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-time-minLength-3"
        namespace = "NISTSchema-SV-IV-list-time-minLength-3-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            min_length=7.0
        )
    )