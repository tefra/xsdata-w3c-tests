from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-hexBinary-minLength-3-NS"


@dataclass
class NistschemaSvIvListHexBinaryMinLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-hexBinary-minLength-3"
        namespace = "NISTSchema-SV-IV-list-hexBinary-minLength-3-NS"

    value: List[bytes] = field(
        default_factory=list,
        metadata={
            "min_length": 7,
            "tokens": True,
            "format": "base16",
        }
    )
