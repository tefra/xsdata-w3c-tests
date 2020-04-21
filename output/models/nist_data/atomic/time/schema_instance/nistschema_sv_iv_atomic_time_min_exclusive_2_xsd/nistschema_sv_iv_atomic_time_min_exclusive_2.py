from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-minExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicTimeMinExclusive2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-minExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-time-minExclusive-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            min_exclusive="02:57:29"
        )
    )
