from dataclasses import dataclass, field
from datetime import time
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-time-minLength-4-NS"


@dataclass
class NistschemaSvIvListTimeMinLength4:
    class Meta:
        name = "NISTSchema-SV-IV-list-time-minLength-4"
        namespace = "NISTSchema-SV-IV-list-time-minLength-4-NS"

    value: List[time] = field(
        default_factory=list,
        metadata={
            "required": True,
            "min_length": 8,
            "tokens": True,
        }
    )
