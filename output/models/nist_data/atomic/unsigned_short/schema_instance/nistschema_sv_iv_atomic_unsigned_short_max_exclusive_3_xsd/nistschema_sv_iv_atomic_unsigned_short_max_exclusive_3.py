from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedShort-maxExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedShortMaxExclusive3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedShort-maxExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-unsignedShort-maxExclusive-3-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": 64347,
        }
    )
