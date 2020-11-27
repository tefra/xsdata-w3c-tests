from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-positiveInteger-totalDigits-1-NS"


@dataclass
class NistschemaSvIvAtomicPositiveIntegerTotalDigits1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-positiveInteger-totalDigits-1"
        namespace = "NISTSchema-SV-IV-atomic-positiveInteger-totalDigits-1-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "total_digits": 1,
        }
    )
