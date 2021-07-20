from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedLong-totalDigits-5-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedLongTotalDigits5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedLong-totalDigits-5"
        namespace = "NISTSchema-SV-IV-atomic-unsignedLong-totalDigits-5-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "total_digits": 18,
        }
    )
