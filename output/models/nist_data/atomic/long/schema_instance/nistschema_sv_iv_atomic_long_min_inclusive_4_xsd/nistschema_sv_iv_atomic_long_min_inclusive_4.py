from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-long-minInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicLongMinInclusive4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-long-minInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-long-minInclusive-4-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            min_inclusive=5.794513869292511e+17
        )
    )
