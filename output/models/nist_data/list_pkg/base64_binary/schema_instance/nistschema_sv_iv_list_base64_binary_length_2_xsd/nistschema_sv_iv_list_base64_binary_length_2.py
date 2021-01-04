from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-base64Binary-length-2-NS"


@dataclass
class NistschemaSvIvListBase64BinaryLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-base64Binary-length-2"
        namespace = "NISTSchema-SV-IV-list-base64Binary-length-2-NS"

    value: List[bytes] = field(
        default_factory=list,
        metadata={
            "required": True,
            "length": 6,
            "tokens": True,
            "format": "base64",
        }
    )
