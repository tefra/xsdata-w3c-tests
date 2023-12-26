from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-integer-minExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicIntegerMinExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-integer-minExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-integer-minExclusive-3-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": 389578809107570477,
        },
    )
