from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-integer-maxExclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicIntegerMaxExclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-integer-maxExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-integer-maxExclusive-5-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "max_exclusive": 999999999999999999,
        }
    )
