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
        metadata={
            "required": True,
            "min_length": 6,
            "tokens": True,
        }
    )
