from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonPositiveInteger-totalDigits-3-NS"


@dataclass
class NistschemaSvIvAtomicNonPositiveIntegerTotalDigits3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonPositiveInteger-totalDigits-3"
        namespace = "NISTSchema-SV-IV-atomic-nonPositiveInteger-totalDigits-3-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "total_digits": 9,
        }
    )
