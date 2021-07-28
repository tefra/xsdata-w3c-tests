from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-hexBinary-maxLength-3-NS"


@dataclass
class NistschemaSvIvAtomicHexBinaryMaxLength3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-hexBinary-maxLength-3"
        namespace = "NISTSchema-SV-IV-atomic-hexBinary-maxLength-3-NS"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "required": True,
            "max_length": 7,
            "format": "base16",
        }
    )
