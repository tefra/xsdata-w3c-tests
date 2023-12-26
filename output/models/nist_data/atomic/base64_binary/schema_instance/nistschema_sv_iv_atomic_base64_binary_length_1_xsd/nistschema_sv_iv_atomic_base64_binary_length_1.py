from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-base64Binary-length-1-NS"


@dataclass
class NistschemaSvIvAtomicBase64BinaryLength1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-base64Binary-length-1"
        namespace = "NISTSchema-SV-IV-atomic-base64Binary-length-1-NS"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "required": True,
            "length": 1,
            "format": "base64",
        },
    )
