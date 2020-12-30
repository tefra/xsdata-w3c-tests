from dataclasses import dataclass, field
from datetime import time
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-time-length-3-NS"


@dataclass
class NistschemaSvIvListTimeLength3:
    class Meta:
        name = "NISTSchema-SV-IV-list-time-length-3"
        namespace = "NISTSchema-SV-IV-list-time-length-3-NS"

    value: List[time] = field(
        default_factory=list,
        metadata={
            "required": True,
            "length": 7,
            "tokens": True,
        }
    )
