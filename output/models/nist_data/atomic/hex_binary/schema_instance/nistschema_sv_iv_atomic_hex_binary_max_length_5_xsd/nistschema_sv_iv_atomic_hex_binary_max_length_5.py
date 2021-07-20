from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-hexBinary-maxLength-5-NS"


@dataclass
class NistschemaSvIvAtomicHexBinaryMaxLength5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-hexBinary-maxLength-5"
        namespace = "NISTSchema-SV-IV-atomic-hexBinary-maxLength-5-NS"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "max_length": 74,
            "format": "base16",
        }
    )
