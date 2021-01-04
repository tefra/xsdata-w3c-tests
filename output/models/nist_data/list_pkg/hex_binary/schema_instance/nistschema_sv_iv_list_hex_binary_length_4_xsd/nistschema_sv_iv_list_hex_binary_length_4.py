from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-hexBinary-length-4-NS"


@dataclass
class NistschemaSvIvListHexBinaryLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-hexBinary-length-4"
        namespace = "NISTSchema-SV-IV-list-hexBinary-length-4-NS"

    value: List[bytes] = field(
        default_factory=list,
        metadata={
            "required": True,
            "length": 8,
            "tokens": True,
            "format": "base16",
        }
    )
