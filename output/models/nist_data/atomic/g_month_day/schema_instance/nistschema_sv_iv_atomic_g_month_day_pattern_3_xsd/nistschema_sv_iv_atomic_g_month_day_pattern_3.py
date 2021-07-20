from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonthDay-pattern-3-NS"


@dataclass
class NistschemaSvIvAtomicGMonthDayPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonthDay-pattern-3"
        namespace = "NISTSchema-SV-IV-atomic-gMonthDay-pattern-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "pattern": r"--0\d-\d8",
        }
    )
