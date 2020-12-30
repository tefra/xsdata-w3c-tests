from dataclasses import dataclass, field
from datetime import time
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-minInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicTimeMinInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-minInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-time-minInclusive-4-NS"

    value: Optional[time] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": time(19, 31, 35),
        }
    )
