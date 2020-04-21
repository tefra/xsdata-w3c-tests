from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-long-minExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicLongMinExclusive3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-long-minExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-long-minExclusive-3-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            min_exclusive=4.2071598181571136e+17
        )
    )
