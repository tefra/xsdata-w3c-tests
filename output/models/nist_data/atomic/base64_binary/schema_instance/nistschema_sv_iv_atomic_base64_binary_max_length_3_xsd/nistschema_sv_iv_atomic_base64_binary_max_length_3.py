from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-base64Binary-maxLength-3-NS"


@dataclass
class NistschemaSvIvAtomicBase64BinaryMaxLength3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-base64Binary-maxLength-3"
        namespace = "NISTSchema-SV-IV-atomic-base64Binary-maxLength-3-NS"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "required": True,
            "max_length": 54,
            "format": "base64",
        },
    )
