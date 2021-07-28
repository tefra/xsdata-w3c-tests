from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-minExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedIntMinExclusive2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedInt-minExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-unsignedInt-minExclusive-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": 72170852,
        }
    )
