from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-int-totalDigits-5-NS"


@dataclass
class NistschemaSvIvAtomicIntTotalDigits5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-int-totalDigits-5"
        namespace = "NISTSchema-SV-IV-atomic-int-totalDigits-5-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "total_digits": 10,
        }
    )
