from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonthDay-pattern-5-NS"


@dataclass
class NistschemaSvIvAtomicGMonthDayPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonthDay-pattern-5"
        namespace = "NISTSchema-SV-IV-atomic-gMonthDay-pattern-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"--0\d-1\d",
        }
    )
