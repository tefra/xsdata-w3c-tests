from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-nonPositiveInteger-whiteSpace-1-NS"


@dataclass
class NistschemaSvIvListNonPositiveIntegerWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-list-nonPositiveInteger-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-list-nonPositiveInteger-whiteSpace-1-NS"

    value: List[int] = field(
        default_factory=list,
        metadata={
            "white_space": "collapse",
            "tokens": True,
        },
    )
