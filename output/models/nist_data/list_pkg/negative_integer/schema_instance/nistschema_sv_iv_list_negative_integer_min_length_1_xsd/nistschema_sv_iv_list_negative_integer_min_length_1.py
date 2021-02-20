from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-negativeInteger-minLength-1-NS"


@dataclass
class NistschemaSvIvListNegativeIntegerMinLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-negativeInteger-minLength-1"
        namespace = "NISTSchema-SV-IV-list-negativeInteger-minLength-1-NS"

    value: List[int] = field(
        default_factory=list,
        metadata={
            "min_length": 5,
            "tokens": True,
        }
    )
