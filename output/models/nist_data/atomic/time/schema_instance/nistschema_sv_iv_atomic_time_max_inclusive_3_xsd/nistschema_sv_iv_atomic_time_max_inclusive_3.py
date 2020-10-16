from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-time-maxInclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicTimeMaxInclusive3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-time-maxInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-time-maxInclusive-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": "05:07:34",
        }
    )
