from dataclasses import dataclass, field
from datetime import time
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-maxExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicTimeMaxExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-maxExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-time-maxExclusive-2-NS"

    value: Optional[time] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": time(8, 19, 11),
        }
    )
