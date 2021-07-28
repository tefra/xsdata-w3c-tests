from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-base64Binary-length-2-NS"


@dataclass
class NistschemaSvIvAtomicBase64BinaryLength2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-base64Binary-length-2"
        namespace = "NISTSchema-SV-IV-atomic-base64Binary-length-2-NS"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "required": True,
            "length": 1,
            "format": "base64",
        }
    )
