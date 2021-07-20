from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-negativeInteger-totalDigits-2-NS"


@dataclass
class NistschemaSvIvAtomicNegativeIntegerTotalDigits2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-negativeInteger-totalDigits-2"
        namespace = "NISTSchema-SV-IV-atomic-negativeInteger-totalDigits-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "total_digits": 5,
        }
    )
