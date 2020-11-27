from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-integer-minExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicIntegerMinExclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-integer-minExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-integer-minExclusive-4-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": 470740450062970382,
        }
    )
