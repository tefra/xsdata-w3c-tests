from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-byte-minInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicByteMinInclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-byte-minInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-byte-minInclusive-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "min_inclusive": 35,
        }
    )
