from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-double-maxLength-3-NS"


@dataclass
class NistschemaSvIvListDoubleMaxLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-double-maxLength-3"
        namespace = "NISTSchema-SV-IV-list-double-maxLength-3-NS"

    value: List[float] = field(
        default_factory=list,
        metadata={
            "max_length": 7,
            "tokens": True,
        },
    )
