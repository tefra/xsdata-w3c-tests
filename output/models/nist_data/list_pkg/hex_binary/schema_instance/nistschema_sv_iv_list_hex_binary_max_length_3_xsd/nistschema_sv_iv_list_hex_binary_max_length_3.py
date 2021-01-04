from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-hexBinary-maxLength-3-NS"


@dataclass
class NistschemaSvIvListHexBinaryMaxLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-hexBinary-maxLength-3"
        namespace = "NISTSchema-SV-IV-list-hexBinary-maxLength-3-NS"

    value: List[bytes] = field(
        default_factory=list,
        metadata={
            "required": True,
            "max_length": 7,
            "tokens": True,
            "format": "base16",
        }
    )
