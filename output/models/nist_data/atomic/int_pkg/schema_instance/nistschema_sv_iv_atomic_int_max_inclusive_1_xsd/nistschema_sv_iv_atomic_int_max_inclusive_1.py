from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-int-maxInclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicIntMaxInclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-int-maxInclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-int-maxInclusive-1-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "max_inclusive": -2147483648,
        }
    )
