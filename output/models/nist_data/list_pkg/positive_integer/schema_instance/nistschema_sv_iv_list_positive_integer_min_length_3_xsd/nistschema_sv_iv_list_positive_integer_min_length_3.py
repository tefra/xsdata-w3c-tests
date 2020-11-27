from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-positiveInteger-minLength-3-NS"


@dataclass
class NistschemaSvIvListPositiveIntegerMinLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-positiveInteger-minLength-3"
        namespace = "NISTSchema-SV-IV-list-positiveInteger-minLength-3-NS"

    value: List[int] = field(
        default_factory=list,
        metadata={
            "required": True,
            "min_length": 7,
            "tokens": True,
        }
    )
