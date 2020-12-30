from dataclasses import dataclass, field
from datetime import time
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-maxInclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicTimeMaxInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-maxInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-time-maxInclusive-3-NS"

    value: Optional[time] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": time(5, 7, 34),
        }
    )
