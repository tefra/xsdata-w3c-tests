from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-token-length-1-NS"


@dataclass
class NistschemaSvIvAtomicTokenLength1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-token-length-1"
        namespace = "NISTSchema-SV-IV-atomic-token-length-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "length": 0,
        }
    )
