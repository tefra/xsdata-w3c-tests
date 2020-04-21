from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonthDay-pattern-2-NS"


@dataclass
class NistschemaSvIvAtomicGMonthDayPattern2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonthDay-pattern-2"
        namespace = "NISTSchema-SV-IV-atomic-gMonthDay-pattern-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            pattern=r"--\d1-2\d"
        )
    )
