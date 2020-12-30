from dataclasses import dataclass, field
from datetime import time
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-maxInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicTimeMaxInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-maxInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-time-maxInclusive-4-NS"

    value: Optional[time] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": time(18, 6, 59),
        }
    )
