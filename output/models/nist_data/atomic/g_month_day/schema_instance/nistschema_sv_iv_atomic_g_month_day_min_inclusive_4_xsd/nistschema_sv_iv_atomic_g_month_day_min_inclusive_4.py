from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonthDay-minInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicGMonthDayMinInclusive4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonthDay-minInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-gMonthDay-minInclusive-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            min_inclusive="--03-04"
        )
    )
