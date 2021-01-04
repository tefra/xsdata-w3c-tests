from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-hexBinary-minLength-4-NS"


@dataclass
class NistschemaSvIvListHexBinaryMinLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-hexBinary-minLength-4"
        namespace = "NISTSchema-SV-IV-list-hexBinary-minLength-4-NS"

    value: List[bytes] = field(
        default_factory=list,
        metadata={
            "required": True,
            "min_length": 8,
            "tokens": True,
            "format": "base16",
        }
    )
