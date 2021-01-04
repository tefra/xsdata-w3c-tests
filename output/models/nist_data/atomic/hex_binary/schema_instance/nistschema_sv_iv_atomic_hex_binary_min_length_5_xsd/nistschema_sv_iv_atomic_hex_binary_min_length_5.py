from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-hexBinary-minLength-5-NS"


@dataclass
class NistschemaSvIvAtomicHexBinaryMinLength5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-hexBinary-minLength-5"
        namespace = "NISTSchema-SV-IV-atomic-hexBinary-minLength-5-NS"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "required": True,
            "min_length": 74,
            "format": "base16",
        }
    )
