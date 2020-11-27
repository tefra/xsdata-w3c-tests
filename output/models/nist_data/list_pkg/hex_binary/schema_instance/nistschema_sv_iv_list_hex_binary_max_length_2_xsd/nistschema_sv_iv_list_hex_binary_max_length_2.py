from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-hexBinary-maxLength-2-NS"


@dataclass
class NistschemaSvIvListHexBinaryMaxLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-hexBinary-maxLength-2"
        namespace = "NISTSchema-SV-IV-list-hexBinary-maxLength-2-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "max_length": 6,
            "tokens": True,
        }
    )
