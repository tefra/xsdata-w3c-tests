from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-double-maxLength-1-NS"


@dataclass
class NistschemaSvIvListDoubleMaxLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-double-maxLength-1"
        namespace = "NISTSchema-SV-IV-list-double-maxLength-1-NS"

    value: List[float] = field(
        default_factory=list,
        metadata={
            "max_length": 5,
            "tokens": True,
        }
    )
