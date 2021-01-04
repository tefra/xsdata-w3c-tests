from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-hexBinary-maxLength-1-NS"


@dataclass
class NistschemaSvIvAtomicHexBinaryMaxLength1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-hexBinary-maxLength-1"
        namespace = "NISTSchema-SV-IV-atomic-hexBinary-maxLength-1-NS"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "required": True,
            "max_length": 1,
            "format": "base16",
        }
    )
