from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonthDay-minExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicGMonthDayMinExclusive4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonthDay-minExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-gMonthDay-minExclusive-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            min_exclusive="--01-01"
        )
    )