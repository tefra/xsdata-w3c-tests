from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedShort-minExclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedShortMinExclusive1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedShort-minExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-unsignedShort-minExclusive-1-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": 0,
        },
    )
