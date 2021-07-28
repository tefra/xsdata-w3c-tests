from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-int-minInclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicIntMinInclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-int-minInclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-int-minInclusive-5-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": 2147483647,
        }
    )
