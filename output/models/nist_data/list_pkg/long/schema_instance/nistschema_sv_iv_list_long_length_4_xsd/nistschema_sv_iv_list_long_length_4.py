from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-long-length-4-NS"


@dataclass
class NistschemaSvIvListLongLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-long-length-4"
        namespace = "NISTSchema-SV-IV-list-long-length-4-NS"

    value: List[int] = field(
        default_factory=list,
        metadata={
            "required": True,
            "length": 8,
            "tokens": True,
        }
    )
