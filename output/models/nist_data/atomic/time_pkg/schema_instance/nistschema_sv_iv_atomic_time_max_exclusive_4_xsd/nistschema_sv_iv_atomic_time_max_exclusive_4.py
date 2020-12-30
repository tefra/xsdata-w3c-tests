from dataclasses import dataclass, field
from datetime import time
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-maxExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicTimeMaxExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-maxExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-time-maxExclusive-4-NS"

    value: Optional[time] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": time(12, 25, 37),
        }
    )
