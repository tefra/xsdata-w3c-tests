from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-integer-maxInclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicIntegerMaxInclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-integer-maxInclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-integer-maxInclusive-5-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "max_inclusive": 999999999999999999,
        }
    )
