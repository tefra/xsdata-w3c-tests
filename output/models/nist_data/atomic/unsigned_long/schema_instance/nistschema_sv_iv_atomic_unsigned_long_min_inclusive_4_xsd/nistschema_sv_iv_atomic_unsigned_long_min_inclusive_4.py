from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedLong-minInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedLongMinInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedLong-minInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-unsignedLong-minInclusive-4-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "min_inclusive": 237916309768272493,
        }
    )
