from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-integer-maxInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicIntegerMaxInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-integer-maxInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-integer-maxInclusive-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": 828008406281169228,
        },
    )
