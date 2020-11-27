from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-anyURI-maxLength-1-NS"


@dataclass
class NistschemaSvIvAtomicAnyUriMaxLength1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-anyURI-maxLength-1"
        namespace = "NISTSchema-SV-IV-atomic-anyURI-maxLength-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "max_length": 11,
        }
    )
