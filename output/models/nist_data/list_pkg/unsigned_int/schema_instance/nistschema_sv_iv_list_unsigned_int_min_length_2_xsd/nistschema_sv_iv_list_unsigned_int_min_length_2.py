from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedInt-minLength-2-NS"


@dataclass
class NistschemaSvIvListUnsignedIntMinLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedInt-minLength-2"
        namespace = "NISTSchema-SV-IV-list-unsignedInt-minLength-2-NS"

    value: List[int] = field(
        default_factory=list,
        metadata={
            "min_length": 6,
            "tokens": True,
        }
    )
