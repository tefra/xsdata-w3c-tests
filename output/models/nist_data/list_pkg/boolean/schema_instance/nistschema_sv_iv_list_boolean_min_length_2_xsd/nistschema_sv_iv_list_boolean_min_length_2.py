from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-boolean-minLength-2-NS"


@dataclass
class NistschemaSvIvListBooleanMinLength2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-boolean-minLength-2"
        namespace = "NISTSchema-SV-IV-list-boolean-minLength-2-NS"

    value: List[bool] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            min_length=6
        )
    )
