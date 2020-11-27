from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-boolean-minLength-4-NS"


@dataclass
class NistschemaSvIvListBooleanMinLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-boolean-minLength-4"
        namespace = "NISTSchema-SV-IV-list-boolean-minLength-4-NS"

    value: List[bool] = field(
        default_factory=list,
        metadata={
            "required": True,
            "min_length": 8,
            "tokens": True,
        }
    )
