from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-long-minExclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicLongMinExclusive1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-long-minExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-long-minExclusive-1-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            min_exclusive=-1e+18
        )
    )
