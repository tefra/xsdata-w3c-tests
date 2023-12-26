from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedByte-minLength-3-NS"


@dataclass
class NistschemaSvIvListUnsignedByteMinLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedByte-minLength-3"
        namespace = "NISTSchema-SV-IV-list-unsignedByte-minLength-3-NS"

    value: List[int] = field(
        default_factory=list,
        metadata={
            "min_length": 7,
            "tokens": True,
        },
    )
