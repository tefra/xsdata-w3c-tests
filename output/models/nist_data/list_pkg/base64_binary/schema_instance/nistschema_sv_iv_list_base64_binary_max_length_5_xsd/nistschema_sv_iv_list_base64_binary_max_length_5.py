from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-base64Binary-maxLength-5-NS"


@dataclass
class NistschemaSvIvListBase64BinaryMaxLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-base64Binary-maxLength-5"
        namespace = "NISTSchema-SV-IV-list-base64Binary-maxLength-5-NS"

    value: List[bytes] = field(
        default_factory=list,
        metadata={
            "max_length": 10,
            "tokens": True,
            "format": "base64",
        }
    )
