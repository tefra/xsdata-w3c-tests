from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedByte-minExclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedByteMinExclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedByte-minExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-unsignedByte-minExclusive-5-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "min_exclusive": 254,
        }
    )
