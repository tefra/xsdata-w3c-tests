from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-hexBinary-length-3-NS"


@dataclass
class NistschemaSvIvAtomicHexBinaryLength3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-hexBinary-length-3"
        namespace = "NISTSchema-SV-IV-atomic-hexBinary-length-3-NS"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "length": 41,
            "format": "base16",
        }
    )
