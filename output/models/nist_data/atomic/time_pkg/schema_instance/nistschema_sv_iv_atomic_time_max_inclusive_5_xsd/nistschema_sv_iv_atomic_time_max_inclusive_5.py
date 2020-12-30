from dataclasses import dataclass, field
from datetime import time
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-maxInclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicTimeMaxInclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-maxInclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-time-maxInclusive-5-NS"

    value: Optional[time] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": time(23, 59, 59),
        }
    )
