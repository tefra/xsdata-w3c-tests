from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-base64Binary-whiteSpace-1-NS"


@dataclass
class NistschemaSvIvListBase64BinaryWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-list-base64Binary-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-list-base64Binary-whiteSpace-1-NS"

    value: List[bytes] = field(
        default_factory=list,
        metadata={
            "required": True,
            "white_space": "collapse",
            "tokens": True,
            "format": "base64",
        }
    )
