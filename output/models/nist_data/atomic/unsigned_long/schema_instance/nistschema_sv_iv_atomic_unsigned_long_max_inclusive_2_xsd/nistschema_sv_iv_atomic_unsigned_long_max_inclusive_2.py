from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedLong-maxInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedLongMaxInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedLong-maxInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-unsignedLong-maxInclusive-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": 183206970010490244,
        },
    )
