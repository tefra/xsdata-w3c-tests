from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-boolean-minLength-1-NS"


@dataclass
class NistschemaSvIvListBooleanMinLength1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-list-boolean-minLength-1"
        namespace = "NISTSchema-SV-IV-list-boolean-minLength-1-NS"

    value: List[bool] = field(
        default_factory=list,
        metadata=dict(
            required=True,
            min_length=5,
            tokens=True
        )
    )
