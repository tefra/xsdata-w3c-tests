from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedLong-maxExclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedLongMaxExclusive1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedLong-maxExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-unsignedLong-maxExclusive-1-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": 1,
        }
    )
