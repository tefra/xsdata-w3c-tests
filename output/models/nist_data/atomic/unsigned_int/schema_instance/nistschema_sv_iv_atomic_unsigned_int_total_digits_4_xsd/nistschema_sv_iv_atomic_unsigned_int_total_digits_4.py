from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-totalDigits-4-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedIntTotalDigits4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedInt-totalDigits-4"
        namespace = "NISTSchema-SV-IV-atomic-unsignedInt-totalDigits-4-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "total_digits": 7,
        },
    )
