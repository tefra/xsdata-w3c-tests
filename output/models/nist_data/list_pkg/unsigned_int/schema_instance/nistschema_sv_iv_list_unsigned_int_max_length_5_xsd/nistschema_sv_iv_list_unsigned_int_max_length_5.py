from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-unsignedInt-maxLength-5-NS"


@dataclass
class NistschemaSvIvListUnsignedIntMaxLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-unsignedInt-maxLength-5"
        namespace = "NISTSchema-SV-IV-list-unsignedInt-maxLength-5-NS"

    value: List[int] = field(
        default_factory=list,
        metadata={
            "required": True,
            "max_length": 10,
            "tokens": True,
        }
    )
