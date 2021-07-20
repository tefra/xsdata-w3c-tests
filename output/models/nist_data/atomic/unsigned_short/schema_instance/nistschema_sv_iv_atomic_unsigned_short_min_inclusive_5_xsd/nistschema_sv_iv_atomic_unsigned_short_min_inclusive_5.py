from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedShort-minInclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedShortMinInclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedShort-minInclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-unsignedShort-minInclusive-5-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "min_inclusive": 65535,
        }
    )
