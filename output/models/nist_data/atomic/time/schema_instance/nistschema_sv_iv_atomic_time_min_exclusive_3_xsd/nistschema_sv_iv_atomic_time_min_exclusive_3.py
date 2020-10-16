from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-minExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicTimeMinExclusive3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-minExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-time-minExclusive-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": "13:38:10",
        }
    )
