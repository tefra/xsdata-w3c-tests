from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-token-length-2-NS"


@dataclass
class NistschemaSvIvAtomicTokenLength2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-token-length-2"
        namespace = "NISTSchema-SV-IV-atomic-token-length-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "length": 295,
        }
    )
