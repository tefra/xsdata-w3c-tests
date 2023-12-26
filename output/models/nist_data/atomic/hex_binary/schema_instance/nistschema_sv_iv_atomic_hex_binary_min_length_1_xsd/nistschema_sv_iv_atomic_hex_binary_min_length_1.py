from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-hexBinary-minLength-1-NS"


@dataclass
class NistschemaSvIvAtomicHexBinaryMinLength1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-hexBinary-minLength-1"
        namespace = "NISTSchema-SV-IV-atomic-hexBinary-minLength-1-NS"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "required": True,
            "min_length": 1,
            "format": "base16",
        },
    )
