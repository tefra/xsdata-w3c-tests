from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-hexBinary-length-5-NS"


@dataclass
class NistschemaSvIvListHexBinaryLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-hexBinary-length-5"
        namespace = "NISTSchema-SV-IV-list-hexBinary-length-5-NS"

    value: List[bytes] = field(
        default_factory=list,
        metadata={
            "required": True,
            "length": 10,
            "tokens": True,
            "format": "base16",
        }
    )
