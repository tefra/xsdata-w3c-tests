from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-base64Binary-maxLength-2-NS"


@dataclass
class NistschemaSvIvAtomicBase64BinaryMaxLength2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-base64Binary-maxLength-2"
        namespace = "NISTSchema-SV-IV-atomic-base64Binary-maxLength-2-NS"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "max_length": 45,
            "format": "base64",
        }
    )
