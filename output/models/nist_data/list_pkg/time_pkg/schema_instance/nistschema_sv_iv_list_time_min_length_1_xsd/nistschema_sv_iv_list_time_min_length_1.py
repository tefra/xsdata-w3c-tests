from dataclasses import dataclass, field
from datetime import time
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-time-minLength-1-NS"


@dataclass
class NistschemaSvIvListTimeMinLength1:
    class Meta:
        name = "NISTSchema-SV-IV-list-time-minLength-1"
        namespace = "NISTSchema-SV-IV-list-time-minLength-1-NS"

    value: List[time] = field(
        default_factory=list,
        metadata={
            "required": True,
            "min_length": 5,
            "tokens": True,
        }
    )