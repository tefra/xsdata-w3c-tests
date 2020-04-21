from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-maxExclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicTimeMaxExclusive1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-maxExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-time-maxExclusive-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            max_exclusive="00:00:01"
        )
    )
