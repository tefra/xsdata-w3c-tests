from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-integer-maxLength-2-NS"


@dataclass
class NistschemaSvIvListIntegerMaxLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-integer-maxLength-2"
        namespace = "NISTSchema-SV-IV-list-integer-maxLength-2-NS"

    value: List[int] = field(
        default_factory=list,
        metadata={
            "max_length": 6,
            "tokens": True,
        },
    )
