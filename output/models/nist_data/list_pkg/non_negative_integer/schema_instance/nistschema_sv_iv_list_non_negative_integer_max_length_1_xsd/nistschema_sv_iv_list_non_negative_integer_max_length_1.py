from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-nonNegativeInteger-maxLength-1-NS"


@dataclass
class NistschemaSvIvListNonNegativeIntegerMaxLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-nonNegativeInteger-maxLength-1"
        namespace = "NISTSchema-SV-IV-list-nonNegativeInteger-maxLength-1-NS"

    value: List[int] = field(
        default_factory=list,
        metadata={
            "max_length": 5,
            "tokens": True,
        }
    )
