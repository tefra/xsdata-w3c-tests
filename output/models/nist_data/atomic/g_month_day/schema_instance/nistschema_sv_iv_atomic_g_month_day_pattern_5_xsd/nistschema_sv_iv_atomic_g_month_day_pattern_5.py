from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonthDay-pattern-5-NS"


@dataclass
class NistschemaSvIvAtomicGMonthDayPattern5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonthDay-pattern-5"
        namespace = "NISTSchema-SV-IV-atomic-gMonthDay-pattern-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            pattern=r"--0\d-1\d"
        )
    )
