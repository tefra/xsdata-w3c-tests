from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedByte-maxInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedByteMaxInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedByte-maxInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-unsignedByte-maxInclusive-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": 232,
        },
    )
