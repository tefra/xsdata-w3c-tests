from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-byte-totalDigits-1-NS"


@dataclass
class NistschemaSvIvAtomicByteTotalDigits1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-byte-totalDigits-1"
        namespace = "NISTSchema-SV-IV-atomic-byte-totalDigits-1-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "total_digits": 1,
        }
    )
