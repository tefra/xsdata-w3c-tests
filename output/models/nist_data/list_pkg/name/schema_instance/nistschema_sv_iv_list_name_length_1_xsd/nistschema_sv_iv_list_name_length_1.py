from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-Name-length-1-NS"


@dataclass
class NistschemaSvIvListNameLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-Name-length-1"
        namespace = "NISTSchema-SV-IV-list-Name-length-1-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "length": 5,
            "tokens": True,
        },
    )
