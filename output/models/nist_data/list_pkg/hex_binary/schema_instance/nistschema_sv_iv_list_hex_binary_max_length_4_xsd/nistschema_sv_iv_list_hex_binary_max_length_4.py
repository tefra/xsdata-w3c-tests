from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-hexBinary-maxLength-4-NS"


@dataclass
class NistschemaSvIvListHexBinaryMaxLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-hexBinary-maxLength-4"
        namespace = "NISTSchema-SV-IV-list-hexBinary-maxLength-4-NS"

    value: List[bytes] = field(
        default_factory=list,
        metadata={
            "max_length": 8,
            "tokens": True,
            "format": "base16",
        },
    )
