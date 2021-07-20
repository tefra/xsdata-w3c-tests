from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-integer-maxInclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicIntegerMaxInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-integer-maxInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-integer-maxInclusive-3-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "max_inclusive": 705179181121327491,
        }
    )
