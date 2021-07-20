from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-anyURI-minLength-2-NS"


@dataclass
class NistschemaSvIvAtomicAnyUriMinLength2:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-anyURI-minLength-2"
        namespace = "NISTSchema-SV-IV-atomic-anyURI-minLength-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "min_length": 41,
        }
    )
