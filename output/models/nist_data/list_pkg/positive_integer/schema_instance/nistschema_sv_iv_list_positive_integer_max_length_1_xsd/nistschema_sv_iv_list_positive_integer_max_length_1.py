from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-positiveInteger-maxLength-1-NS"


@dataclass
class NistschemaSvIvListPositiveIntegerMaxLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-positiveInteger-maxLength-1"
        namespace = "NISTSchema-SV-IV-list-positiveInteger-maxLength-1-NS"

    value: List[int] = field(
        default_factory=list,
        metadata={
            "required": True,
            "max_length": 5,
            "tokens": True,
        }
    )
