from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedLong-maxExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedLongMaxExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedLong-maxExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-unsignedLong-maxExclusive-3-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": 114762413382550444,
        },
    )
