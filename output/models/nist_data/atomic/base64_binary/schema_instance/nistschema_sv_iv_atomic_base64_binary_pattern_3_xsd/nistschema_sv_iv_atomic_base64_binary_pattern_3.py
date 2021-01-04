from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-base64Binary-pattern-3-NS"


@dataclass
class NistschemaSvIvAtomicBase64BinaryPattern3:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-base64Binary-pattern-3"
        namespace = "NISTSchema-SV-IV-atomic-base64Binary-pattern-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"[a-zA-Z0-9+/]{64}",
            "format": "base64",
        }
    )
