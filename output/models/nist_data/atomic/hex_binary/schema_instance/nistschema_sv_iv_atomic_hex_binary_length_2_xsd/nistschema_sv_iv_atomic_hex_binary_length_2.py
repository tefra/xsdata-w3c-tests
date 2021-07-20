from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-hexBinary-length-2-NS"


@dataclass
class NistschemaSvIvAtomicHexBinaryLength2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-hexBinary-length-2"
        namespace = "NISTSchema-SV-IV-atomic-hexBinary-length-2-NS"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "length": 16,
            "format": "base16",
        }
    )
