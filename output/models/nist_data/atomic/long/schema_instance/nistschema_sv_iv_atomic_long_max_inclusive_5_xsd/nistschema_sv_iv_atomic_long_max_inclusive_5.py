from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-long-maxInclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicLongMaxInclusive5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-long-maxInclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-long-maxInclusive-5-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": 999999999999999999,
        }
    )
