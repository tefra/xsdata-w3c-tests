from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-minInclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicTimeMinInclusive3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-minInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-time-minInclusive-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": "01:03:08",
        }
    )
