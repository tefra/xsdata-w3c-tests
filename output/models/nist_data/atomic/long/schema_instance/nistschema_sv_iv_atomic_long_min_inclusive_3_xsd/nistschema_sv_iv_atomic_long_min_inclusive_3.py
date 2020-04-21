from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-long-minInclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicLongMinInclusive3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-long-minInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-long-minInclusive-3-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            min_inclusive=6.794230316198866e+17
        )
    )
