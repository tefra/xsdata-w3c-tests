from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-float-minLength-4-NS"


@dataclass
class NistschemaSvIvListFloatMinLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-float-minLength-4"
        namespace = "NISTSchema-SV-IV-list-float-minLength-4-NS"

    value: List[float] = field(
        default_factory=list,
        metadata={
            "min_length": 8,
            "tokens": True,
        },
    )
