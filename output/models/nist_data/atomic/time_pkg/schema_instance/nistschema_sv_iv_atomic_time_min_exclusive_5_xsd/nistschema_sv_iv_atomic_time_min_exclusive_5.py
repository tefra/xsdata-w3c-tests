from dataclasses import dataclass, field
from datetime import time
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-minExclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicTimeMinExclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-minExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-time-minExclusive-5-NS"

    value: Optional[time] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": time(23, 59, 58),
        }
    )
