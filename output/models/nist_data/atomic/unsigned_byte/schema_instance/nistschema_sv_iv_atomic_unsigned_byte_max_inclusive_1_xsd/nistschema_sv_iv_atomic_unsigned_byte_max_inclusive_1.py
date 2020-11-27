from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedByte-maxInclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedByteMaxInclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedByte-maxInclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-unsignedByte-maxInclusive-1-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": 0,
        }
    )
