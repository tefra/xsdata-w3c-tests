from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonthDay-maxInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicGMonthDayMaxInclusive4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonthDay-maxInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-gMonthDay-maxInclusive-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            max_inclusive="--07-01"
        )
    )