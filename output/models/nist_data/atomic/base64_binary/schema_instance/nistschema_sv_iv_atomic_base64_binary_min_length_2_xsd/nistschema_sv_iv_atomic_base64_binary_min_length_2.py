from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-base64Binary-minLength-2-NS"


@dataclass
class NistschemaSvIvAtomicBase64BinaryMinLength2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-base64Binary-minLength-2"
        namespace = "NISTSchema-SV-IV-atomic-base64Binary-minLength-2-NS"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "required": True,
            "min_length": 27,
            "format": "base64",
        }
    )
