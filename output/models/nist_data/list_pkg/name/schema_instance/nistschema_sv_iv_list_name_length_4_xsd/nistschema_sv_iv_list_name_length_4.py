from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-Name-length-4-NS"


@dataclass
class NistschemaSvIvListNameLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-Name-length-4"
        namespace = "NISTSchema-SV-IV-list-Name-length-4-NS"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "length": 8,
            "tokens": True,
        }
    )
