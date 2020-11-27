from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-hexBinary-length-5-NS"


@dataclass
class NistschemaSvIvAtomicHexBinaryLength5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-hexBinary-length-5"
        namespace = "NISTSchema-SV-IV-atomic-hexBinary-length-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "length": 74,
        }
    )
