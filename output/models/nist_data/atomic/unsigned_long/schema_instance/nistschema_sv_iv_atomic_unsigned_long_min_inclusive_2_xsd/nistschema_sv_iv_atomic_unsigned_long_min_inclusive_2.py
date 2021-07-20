from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedLong-minInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedLongMinInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedLong-minInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-unsignedLong-minInclusive-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "min_inclusive": 846028599370221122,
        }
    )
