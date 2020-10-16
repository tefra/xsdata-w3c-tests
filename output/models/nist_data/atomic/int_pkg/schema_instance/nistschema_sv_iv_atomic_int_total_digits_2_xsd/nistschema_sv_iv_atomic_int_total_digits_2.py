from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-int-totalDigits-2-NS"


@dataclass
class NistschemaSvIvAtomicIntTotalDigits2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-int-totalDigits-2"
        namespace = "NISTSchema-SV-IV-atomic-int-totalDigits-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "total_digits": 3,
        }
    )
