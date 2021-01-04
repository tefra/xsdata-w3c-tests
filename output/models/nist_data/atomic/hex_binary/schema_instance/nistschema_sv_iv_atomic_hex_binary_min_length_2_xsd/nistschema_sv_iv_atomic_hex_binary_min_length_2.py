from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-hexBinary-minLength-2-NS"


@dataclass
class NistschemaSvIvAtomicHexBinaryMinLength2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-hexBinary-minLength-2"
        namespace = "NISTSchema-SV-IV-atomic-hexBinary-minLength-2-NS"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "required": True,
            "min_length": 28,
            "format": "base16",
        }
    )
