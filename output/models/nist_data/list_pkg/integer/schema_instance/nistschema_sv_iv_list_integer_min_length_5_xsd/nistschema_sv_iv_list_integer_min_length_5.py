from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-integer-minLength-5-NS"


@dataclass
class NistschemaSvIvListIntegerMinLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-integer-minLength-5"
        namespace = "NISTSchema-SV-IV-list-integer-minLength-5-NS"

    value: List[int] = field(
        default_factory=list,
        metadata={
            "min_length": 10,
            "tokens": True,
        },
    )
