from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedInt-minLength-1-NS"


@dataclass
class NistschemaSvIvListUnsignedIntMinLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedInt-minLength-1"
        namespace = "NISTSchema-SV-IV-list-unsignedInt-minLength-1-NS"

    value: List[int] = field(
        default_factory=list,
        metadata={
            "min_length": 5,
            "tokens": True,
        },
    )
