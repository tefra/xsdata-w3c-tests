from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonthDay-maxInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicGMonthDayMaxInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonthDay-maxInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-gMonthDay-maxInclusive-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": "--02-24",
        }
    )
