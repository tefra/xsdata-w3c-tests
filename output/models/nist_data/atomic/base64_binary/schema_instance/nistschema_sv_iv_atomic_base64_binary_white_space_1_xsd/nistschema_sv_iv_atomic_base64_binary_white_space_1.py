from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-base64Binary-whiteSpace-1-NS"


@dataclass
class NistschemaSvIvAtomicBase64BinaryWhiteSpace1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-base64Binary-whiteSpace-1"
        namespace = "NISTSchema-SV-IV-atomic-base64Binary-whiteSpace-1-NS"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "required": True,
            "white_space": "collapse",
            "format": "base64",
        }
    )
