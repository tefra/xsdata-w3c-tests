from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-byte-maxExclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicByteMaxExclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-byte-maxExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-byte-maxExclusive-5-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "max_exclusive": 127,
        }
    )
