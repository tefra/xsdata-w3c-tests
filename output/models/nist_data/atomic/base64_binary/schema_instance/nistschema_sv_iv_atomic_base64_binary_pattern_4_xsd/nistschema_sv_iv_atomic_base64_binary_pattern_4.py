from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-base64Binary-pattern-4-NS"


@dataclass
class NistschemaSvIvAtomicBase64BinaryPattern4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-base64Binary-pattern-4"
        namespace = "NISTSchema-SV-IV-atomic-base64Binary-pattern-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "pattern": r"[a-zA-Z0-9+/]{24}",
        }
    )
