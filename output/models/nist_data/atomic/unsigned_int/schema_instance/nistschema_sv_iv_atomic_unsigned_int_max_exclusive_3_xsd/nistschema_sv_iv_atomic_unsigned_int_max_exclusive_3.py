from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-maxExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedIntMaxExclusive3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedInt-maxExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-unsignedInt-maxExclusive-3-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": 1539442072,
        }
    )
