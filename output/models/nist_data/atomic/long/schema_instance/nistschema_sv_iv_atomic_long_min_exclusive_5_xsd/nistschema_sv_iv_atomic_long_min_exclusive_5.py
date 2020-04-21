from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-long-minExclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicLongMinExclusive5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-long-minExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-long-minExclusive-5-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            min_exclusive=1e+18
        )
    )
