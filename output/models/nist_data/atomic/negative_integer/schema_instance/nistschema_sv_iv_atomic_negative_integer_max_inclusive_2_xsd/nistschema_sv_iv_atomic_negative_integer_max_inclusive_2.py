from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-negativeInteger-maxInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicNegativeIntegerMaxInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-negativeInteger-maxInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-negativeInteger-maxInclusive-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "max_inclusive": -922333322214573646,
        }
    )
