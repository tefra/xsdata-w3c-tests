from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedShort-whiteSpace-1-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedShortWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedShort-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-atomic-unsignedShort-whiteSpace-1-NS"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "white_space": "collapse",
        }
    )
