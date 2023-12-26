from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-negativeInteger-maxInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicNegativeIntegerMaxInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-negativeInteger-maxInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-negativeInteger-maxInclusive-4-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": -666057423564200834,
        },
    )
