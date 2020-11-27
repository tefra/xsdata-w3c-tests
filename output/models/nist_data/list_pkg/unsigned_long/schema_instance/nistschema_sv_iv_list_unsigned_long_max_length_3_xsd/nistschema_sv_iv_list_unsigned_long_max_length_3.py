from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedLong-maxLength-3-NS"


@dataclass
class NistschemaSvIvListUnsignedLongMaxLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedLong-maxLength-3"
        namespace = "NISTSchema-SV-IV-list-unsignedLong-maxLength-3-NS"

    value: List[int] = field(
        default_factory=list,
        metadata={
            "required": True,
            "max_length": 7,
            "tokens": True,
        }
    )
