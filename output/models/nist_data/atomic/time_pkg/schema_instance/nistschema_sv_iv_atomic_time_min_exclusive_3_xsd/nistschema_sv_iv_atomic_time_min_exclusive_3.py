from dataclasses import dataclass, field
from datetime import time
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-minExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicTimeMinExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-minExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-time-minExclusive-3-NS"

    value: Optional[time] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": time(13, 38, 10),
        }
    )
