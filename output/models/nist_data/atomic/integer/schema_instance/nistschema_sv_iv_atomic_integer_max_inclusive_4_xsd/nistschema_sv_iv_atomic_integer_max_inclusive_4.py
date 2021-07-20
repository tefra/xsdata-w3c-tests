from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-integer-maxInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicIntegerMaxInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-integer-maxInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-integer-maxInclusive-4-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "max_inclusive": -2761698266856349,
        }
    )
