from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-int-maxExclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicIntMaxExclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-int-maxExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-int-maxExclusive-5-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "max_exclusive": 2147483647,
        },
    )
