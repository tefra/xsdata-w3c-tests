from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-hexBinary-minLength-1-NS"


@dataclass
class NistschemaSvIvListHexBinaryMinLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-hexBinary-minLength-1"
        namespace = "NISTSchema-SV-IV-list-hexBinary-minLength-1-NS"

    value: List[bytes] = field(
        default_factory=list,
        metadata={
            "min_length": 5,
            "tokens": True,
            "format": "base16",
        },
    )
