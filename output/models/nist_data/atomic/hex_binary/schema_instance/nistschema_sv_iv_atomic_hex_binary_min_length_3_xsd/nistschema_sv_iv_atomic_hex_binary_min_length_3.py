from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-hexBinary-minLength-3-NS"


@dataclass
class NistschemaSvIvAtomicHexBinaryMinLength3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-hexBinary-minLength-3"
        namespace = "NISTSchema-SV-IV-atomic-hexBinary-minLength-3-NS"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "required": True,
            "min_length": 2,
            "format": "base16",
        },
    )
