from dataclasses import dataclass, field
from datetime import time
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-minExclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicTimeMinExclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-minExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-time-minExclusive-1-NS"

    value: Optional[time] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": time(0, 0),
        }
    )
