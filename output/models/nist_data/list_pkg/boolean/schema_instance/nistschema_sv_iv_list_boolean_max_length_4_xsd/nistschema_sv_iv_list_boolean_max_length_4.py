from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-boolean-maxLength-4-NS"


@dataclass
class NistschemaSvIvListBooleanMaxLength4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-boolean-maxLength-4"
        namespace = "NISTSchema-SV-IV-list-boolean-maxLength-4-NS"

    value: List[bool] = field(
        default_factory=list,
        metadata=dict(
            min_occurs=0,
            max_occurs=9223372036854775807,
            max_length=8.0
        )
    )