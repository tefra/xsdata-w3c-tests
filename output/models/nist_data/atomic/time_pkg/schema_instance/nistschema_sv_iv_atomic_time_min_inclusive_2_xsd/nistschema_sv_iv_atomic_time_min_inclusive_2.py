from dataclasses import dataclass, field
from datetime import time
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-minInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicTimeMinInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-minInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-time-minInclusive-2-NS"

    value: Optional[time] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": time(21, 11, 44),
        }
    )
