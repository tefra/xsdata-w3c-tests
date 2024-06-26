from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedShort-minExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedShortMinExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedShort-minExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-unsignedShort-minExclusive-3-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": 42506,
        },
    )
