from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-integer-minInclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicIntegerMinInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-integer-minInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-integer-minInclusive-3-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "min_inclusive": -362471093580558400,
        }
    )
