from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-byte-maxLength-5-NS"


@dataclass
class NistschemaSvIvListByteMaxLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-byte-maxLength-5"
        namespace = "NISTSchema-SV-IV-list-byte-maxLength-5-NS"

    value: List[int] = field(
        default_factory=list,
        metadata={
            "max_length": 10,
            "tokens": True,
        },
    )
