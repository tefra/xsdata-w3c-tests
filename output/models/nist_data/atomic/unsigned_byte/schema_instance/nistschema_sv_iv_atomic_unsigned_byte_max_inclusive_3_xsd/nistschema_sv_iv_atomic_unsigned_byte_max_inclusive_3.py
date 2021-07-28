from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedByte-maxInclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedByteMaxInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedByte-maxInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-unsignedByte-maxInclusive-3-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": 104,
        }
    )
