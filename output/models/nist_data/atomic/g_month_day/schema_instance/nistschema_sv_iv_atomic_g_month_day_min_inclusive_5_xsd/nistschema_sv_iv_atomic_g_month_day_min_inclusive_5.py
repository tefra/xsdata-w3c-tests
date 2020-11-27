from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonthDay-minInclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicGMonthDayMinInclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonthDay-minInclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-gMonthDay-minInclusive-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": "--12-31",
        }
    )
