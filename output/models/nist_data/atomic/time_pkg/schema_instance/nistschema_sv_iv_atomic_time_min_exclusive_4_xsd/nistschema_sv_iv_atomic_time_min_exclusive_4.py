from dataclasses import dataclass, field
from datetime import time
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-minExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicTimeMinExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-minExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-time-minExclusive-4-NS"

    value: Optional[time] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": time(18, 16, 28),
        }
    )
