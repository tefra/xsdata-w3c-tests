from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-short-maxInclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicShortMaxInclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-short-maxInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-short-maxInclusive-3-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": -25835,
        }
    )
