from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonth-maxInclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicGMonthMaxInclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonth-maxInclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-gMonth-maxInclusive-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": "--12",
        }
    )
