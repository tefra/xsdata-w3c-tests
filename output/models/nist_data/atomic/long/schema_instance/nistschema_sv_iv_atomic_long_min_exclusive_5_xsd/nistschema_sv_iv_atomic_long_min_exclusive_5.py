from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-long-minExclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicLongMinExclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-long-minExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-long-minExclusive-5-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": 999999999999999998,
        },
    )
