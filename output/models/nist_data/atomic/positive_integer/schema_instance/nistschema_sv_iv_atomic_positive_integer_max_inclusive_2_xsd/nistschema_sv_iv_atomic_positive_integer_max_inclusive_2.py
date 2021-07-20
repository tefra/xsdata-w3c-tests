from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-positiveInteger-maxInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicPositiveIntegerMaxInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-positiveInteger-maxInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-positiveInteger-maxInclusive-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "max_inclusive": 423285904007674851,
        }
    )
