from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-base64Binary-minLength-1-NS"


@dataclass
class NistschemaSvIvAtomicBase64BinaryMinLength1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-base64Binary-minLength-1"
        namespace = "NISTSchema-SV-IV-atomic-base64Binary-minLength-1-NS"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "min_length": 1,
            "format": "base64",
        }
    )
