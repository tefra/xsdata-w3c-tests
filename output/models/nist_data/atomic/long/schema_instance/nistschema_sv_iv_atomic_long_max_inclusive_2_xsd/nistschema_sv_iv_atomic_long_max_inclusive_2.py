from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-long-maxInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicLongMaxInclusive2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-long-maxInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-long-maxInclusive-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            max_inclusive=4.725124214922365e+17
        )
    )