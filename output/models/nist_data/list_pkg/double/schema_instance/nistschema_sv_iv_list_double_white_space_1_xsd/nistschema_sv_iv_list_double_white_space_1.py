from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-double-whiteSpace-1-NS"


@dataclass
class NistschemaSvIvListDoubleWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-list-double-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-list-double-whiteSpace-1-NS"

    value: List[float] = field(
        default_factory=list,
        metadata={
            "white_space": "collapse",
            "tokens": True,
        },
    )
