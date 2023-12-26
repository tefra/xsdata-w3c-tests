from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-long-maxExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicLongMaxExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-long-maxExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-long-maxExclusive-4-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": -40900034799576711,
        },
    )
