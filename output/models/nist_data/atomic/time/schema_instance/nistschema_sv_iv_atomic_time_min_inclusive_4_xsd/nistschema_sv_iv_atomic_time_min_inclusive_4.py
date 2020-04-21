from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-minInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicTimeMinInclusive4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-minInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-time-minInclusive-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            min_inclusive="19:31:35"
        )
    )
