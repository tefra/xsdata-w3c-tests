from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-hexBinary-length-1-NS"


@dataclass
class NistschemaSvIvListHexBinaryLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-hexBinary-length-1"
        namespace = "NISTSchema-SV-IV-list-hexBinary-length-1-NS"

    value: List[bytes] = field(
        default_factory=list,
        metadata={
            "length": 5,
            "tokens": True,
            "format": "base16",
        },
    )
