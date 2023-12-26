from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-nonNegativeInteger-minLength-5-NS"


@dataclass
class NistschemaSvIvListNonNegativeIntegerMinLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-nonNegativeInteger-minLength-5"
        namespace = "NISTSchema-SV-IV-list-nonNegativeInteger-minLength-5-NS"

    value: List[int] = field(
        default_factory=list,
        metadata={
            "min_length": 10,
            "tokens": True,
        },
    )
