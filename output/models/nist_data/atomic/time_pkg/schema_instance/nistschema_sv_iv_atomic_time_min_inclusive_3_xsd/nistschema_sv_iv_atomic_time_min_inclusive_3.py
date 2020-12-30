from dataclasses import dataclass, field
from datetime import time
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-minInclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicTimeMinInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-minInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-time-minInclusive-3-NS"

    value: Optional[time] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": time(1, 3, 8),
        }
    )
