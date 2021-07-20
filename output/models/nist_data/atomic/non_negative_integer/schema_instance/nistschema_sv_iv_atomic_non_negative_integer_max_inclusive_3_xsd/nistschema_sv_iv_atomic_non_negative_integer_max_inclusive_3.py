from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonNegativeInteger-maxInclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicNonNegativeIntegerMaxInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonNegativeInteger-maxInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-nonNegativeInteger-maxInclusive-3-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "max_inclusive": 154173639038036491,
        }
    )
