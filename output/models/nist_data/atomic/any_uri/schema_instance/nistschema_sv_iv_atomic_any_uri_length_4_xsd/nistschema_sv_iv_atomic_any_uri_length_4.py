from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-anyURI-length-4-NS"


@dataclass
class NistschemaSvIvAtomicAnyUriLength4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-anyURI-length-4"
        namespace = "NISTSchema-SV-IV-atomic-anyURI-length-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "length": 12,
        }
    )
