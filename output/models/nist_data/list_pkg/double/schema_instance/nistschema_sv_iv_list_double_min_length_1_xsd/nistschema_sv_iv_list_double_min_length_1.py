from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-double-minLength-1-NS"


@dataclass
class NistschemaSvIvListDoubleMinLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-double-minLength-1"
        namespace = "NISTSchema-SV-IV-list-double-minLength-1-NS"

    value: List[float] = field(
        default_factory=list,
        metadata={
            "min_length": 5,
            "tokens": True,
        },
    )
