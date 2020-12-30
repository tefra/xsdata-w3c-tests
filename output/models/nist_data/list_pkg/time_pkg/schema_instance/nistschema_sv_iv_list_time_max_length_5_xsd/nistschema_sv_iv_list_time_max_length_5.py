from dataclasses import dataclass, field
from datetime import time
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-time-maxLength-5-NS"


@dataclass
class NistschemaSvIvListTimeMaxLength5:
    class Meta:
        name = "NISTSchema-SV-IV-list-time-maxLength-5"
        namespace = "NISTSchema-SV-IV-list-time-maxLength-5-NS"

    value: List[time] = field(
        default_factory=list,
        metadata={
            "required": True,
            "max_length": 10,
            "tokens": True,
        }
    )
