from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-long-maxInclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicLongMaxInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-long-maxInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-long-maxInclusive-3-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": -319274017545440269,
        }
    )
