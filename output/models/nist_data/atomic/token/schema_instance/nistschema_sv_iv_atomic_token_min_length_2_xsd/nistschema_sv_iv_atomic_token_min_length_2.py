from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-token-minLength-2-NS"


@dataclass
class NistschemaSvIvAtomicTokenMinLength2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-token-minLength-2"
        namespace = "NISTSchema-SV-IV-atomic-token-minLength-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "min_length": 305,
        }
    )
