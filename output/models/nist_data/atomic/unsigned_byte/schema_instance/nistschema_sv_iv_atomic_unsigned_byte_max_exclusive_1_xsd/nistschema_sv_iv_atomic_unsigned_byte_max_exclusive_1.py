from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedByte-maxExclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedByteMaxExclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedByte-maxExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-unsignedByte-maxExclusive-1-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "max_exclusive": 1,
        }
    )
