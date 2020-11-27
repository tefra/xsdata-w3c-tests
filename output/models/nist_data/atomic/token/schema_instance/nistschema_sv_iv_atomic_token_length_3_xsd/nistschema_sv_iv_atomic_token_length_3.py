from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-token-length-3-NS"


@dataclass
class NistschemaSvIvAtomicTokenLength3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-token-length-3"
        namespace = "NISTSchema-SV-IV-atomic-token-length-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "length": 662,
        }
    )
