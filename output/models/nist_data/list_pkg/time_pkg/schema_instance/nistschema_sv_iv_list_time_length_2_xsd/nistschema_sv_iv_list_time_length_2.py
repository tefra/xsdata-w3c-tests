from dataclasses import dataclass, field
from datetime import time
from typing import List

__NAMESPACE__ = "NISTSchema-SV-IV-list-time-length-2-NS"


@dataclass
class NistschemaSvIvListTimeLength2:
    class Meta:
        name = "NISTSchema-SV-IV-list-time-length-2"
        namespace = "NISTSchema-SV-IV-list-time-length-2-NS"

    value: List[time] = field(
        default_factory=list,
        metadata={
            "required": True,
            "length": 6,
            "tokens": True,
        }
    )
