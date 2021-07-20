from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-base64Binary-maxLength-4-NS"


@dataclass
class NistschemaSvIvAtomicBase64BinaryMaxLength4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-base64Binary-maxLength-4"
        namespace = "NISTSchema-SV-IV-atomic-base64Binary-maxLength-4-NS"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "max_length": 61,
            "format": "base64",
        }
    )
