from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedByte-minLength-2-NS"


@dataclass
class NistschemaSvIvListUnsignedByteMinLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedByte-minLength-2"
        namespace = "NISTSchema-SV-IV-list-unsignedByte-minLength-2-NS"

    value: List[int] = field(
        default_factory=list,
        metadata={
            "required": True,
            "min_length": 6,
            "tokens": True,
        }
    )
