from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-minExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedIntMinExclusive3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedInt-minExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-unsignedInt-minExclusive-3-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": 2085810236,
        }
    )
