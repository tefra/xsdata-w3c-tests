from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonPositiveInteger-maxInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicNonPositiveIntegerMaxInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonPositiveInteger-maxInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-nonPositiveInteger-maxInclusive-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "max_inclusive": -63404852978511949,
        }
    )
