from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonNegativeInteger-totalDigits-3-NS"


@dataclass
class NistschemaSvIvAtomicNonNegativeIntegerTotalDigits3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonNegativeInteger-totalDigits-3"
        namespace = "NISTSchema-SV-IV-atomic-nonNegativeInteger-totalDigits-3-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "total_digits": 9,
        }
    )
