from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedByte-totalDigits-2-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedByteTotalDigits2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedByte-totalDigits-2"
        namespace = "NISTSchema-SV-IV-atomic-unsignedByte-totalDigits-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "total_digits": 2,
        },
    )
