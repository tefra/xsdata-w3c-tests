from dataclasses import dataclass, field
from datetime import time
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-time-minLength-5-NS"


@dataclass
class NistschemaSvIvListTimeMinLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-time-minLength-5"
        namespace = "NISTSchema-SV-IV-list-time-minLength-5-NS"

    value: List[time] = field(
        default_factory=list,
        metadata={
            "required": True,
            "min_length": 10,
            "tokens": True,
        }
    )