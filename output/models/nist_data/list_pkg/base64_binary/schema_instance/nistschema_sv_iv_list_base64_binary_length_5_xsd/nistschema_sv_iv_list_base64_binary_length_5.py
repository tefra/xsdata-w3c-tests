from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-base64Binary-length-5-NS"


@dataclass
class NistschemaSvIvListBase64BinaryLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-base64Binary-length-5"
        namespace = "NISTSchema-SV-IV-list-base64Binary-length-5-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "length": 10,
            "tokens": True,
        }
    )
