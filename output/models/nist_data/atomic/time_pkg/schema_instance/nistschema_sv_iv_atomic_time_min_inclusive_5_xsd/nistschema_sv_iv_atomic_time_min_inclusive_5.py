from dataclasses import dataclass, field
from datetime import time
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-minInclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicTimeMinInclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-minInclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-time-minInclusive-5-NS"

    value: Optional[time] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": time(23, 59, 59),
        }
    )
