from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-base64Binary-maxLength-3-NS"


@dataclass
class NistschemaSvIvListBase64BinaryMaxLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-base64Binary-maxLength-3"
        namespace = "NISTSchema-SV-IV-list-base64Binary-maxLength-3-NS"

    value: List[bytes] = field(
        default_factory=list,
        metadata={
            "max_length": 7,
            "tokens": True,
            "format": "base64",
        }
    )
