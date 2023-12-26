from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedLong-maxLength-4-NS"


@dataclass
class NistschemaSvIvListUnsignedLongMaxLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedLong-maxLength-4"
        namespace = "NISTSchema-SV-IV-list-unsignedLong-maxLength-4-NS"

    value: List[int] = field(
        default_factory=list,
        metadata={
            "max_length": 8,
            "tokens": True,
        },
    )
