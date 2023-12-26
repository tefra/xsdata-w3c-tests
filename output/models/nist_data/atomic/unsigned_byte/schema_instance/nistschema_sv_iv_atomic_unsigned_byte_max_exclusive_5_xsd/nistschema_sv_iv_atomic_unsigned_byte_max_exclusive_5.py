from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedByte-maxExclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedByteMaxExclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedByte-maxExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-unsignedByte-maxExclusive-5-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": 255,
        },
    )
