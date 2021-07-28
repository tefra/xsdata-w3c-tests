from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonPositiveInteger-maxInclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicNonPositiveIntegerMaxInclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonPositiveInteger-maxInclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-nonPositiveInteger-maxInclusive-1-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": -999999999999999999,
        }
    )
