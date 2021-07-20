from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-anyURI-maxLength-3-NS"


@dataclass
class NistschemaSvIvAtomicAnyUriMaxLength3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-anyURI-maxLength-3"
        namespace = "NISTSchema-SV-IV-atomic-anyURI-maxLength-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "max_length": 26,
        }
    )
