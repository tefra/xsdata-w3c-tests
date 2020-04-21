from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-gYear-maxLength-1-NS"


@dataclass
class NistschemaSvIvListGYearMaxLength1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-gYear-maxLength-1"
        namespace = "NISTSchema-SV-IV-list-gYear-maxLength-1-NS"

    value: List[str] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            max_length=5.0
        )
    )
