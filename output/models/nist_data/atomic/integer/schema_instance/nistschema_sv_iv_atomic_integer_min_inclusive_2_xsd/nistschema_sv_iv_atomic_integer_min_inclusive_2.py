from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-integer-minInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicIntegerMinInclusive2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-integer-minInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-integer-minInclusive-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": 156487900906511434,
        }
    )
