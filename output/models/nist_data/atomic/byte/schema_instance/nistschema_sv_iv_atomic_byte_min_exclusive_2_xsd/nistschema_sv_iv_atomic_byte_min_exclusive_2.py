from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-byte-minExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicByteMinExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-byte-minExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-byte-minExclusive-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "min_exclusive": 32,
        }
    )
