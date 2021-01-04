from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-base64Binary-pattern-5-NS"


@dataclass
class NistschemaSvIvAtomicBase64BinaryPattern5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-base64Binary-pattern-5"
        namespace = "NISTSchema-SV-IV-atomic-base64Binary-pattern-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"[a-zA-Z0-9+/]{60}",
            "format": "base64",
        }
    )
