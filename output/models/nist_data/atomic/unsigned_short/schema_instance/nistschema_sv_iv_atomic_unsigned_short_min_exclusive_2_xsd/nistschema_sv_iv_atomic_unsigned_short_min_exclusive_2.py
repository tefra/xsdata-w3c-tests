from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedShort-minExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedShortMinExclusive2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedShort-minExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-unsignedShort-minExclusive-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": 40528,
        }
    )
