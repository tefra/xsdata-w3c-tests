from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-maxInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedIntMaxInclusive2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedInt-maxInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-unsignedInt-maxInclusive-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": 3323681229,
        }
    )
