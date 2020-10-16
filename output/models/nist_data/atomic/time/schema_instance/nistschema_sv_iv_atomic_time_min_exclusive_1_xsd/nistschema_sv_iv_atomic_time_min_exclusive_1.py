from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-minExclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicTimeMinExclusive1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-minExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-time-minExclusive-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": "00:00:00",
        }
    )
