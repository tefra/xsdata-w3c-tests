from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonthDay-pattern-1-NS"


@dataclass
class NistschemaSvIvAtomicGMonthDayPattern1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonthDay-pattern-1"
        namespace = "NISTSchema-SV-IV-atomic-gMonthDay-pattern-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"--\d2-1\d",
        }
    )
