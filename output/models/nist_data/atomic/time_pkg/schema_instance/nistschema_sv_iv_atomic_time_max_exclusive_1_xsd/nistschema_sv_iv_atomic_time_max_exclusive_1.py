from dataclasses import dataclass, field
from datetime import time
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-maxExclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicTimeMaxExclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-maxExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-time-maxExclusive-1-NS"

    value: Optional[time] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": time(0, 0, 1),
        }
    )
