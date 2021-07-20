from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-whiteSpace-1-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedIntWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedInt-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-atomic-unsignedInt-whiteSpace-1-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "white_space": "collapse",
        }
    )
