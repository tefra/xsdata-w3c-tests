from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-NMTOKEN-minLength-3-NS"


@dataclass
class NistschemaSvIvListNmtokenMinLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-NMTOKEN-minLength-3"
        namespace = "NISTSchema-SV-IV-list-NMTOKEN-minLength-3-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "min_length": 7,
            "tokens": True,
        },
    )
