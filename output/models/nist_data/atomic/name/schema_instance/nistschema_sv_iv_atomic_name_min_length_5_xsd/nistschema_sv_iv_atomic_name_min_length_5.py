from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-Name-minLength-5-NS"


@dataclass
class NistschemaSvIvAtomicNameMinLength5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-Name-minLength-5"
        namespace = "NISTSchema-SV-IV-atomic-Name-minLength-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "min_length": 64,
        }
    )
