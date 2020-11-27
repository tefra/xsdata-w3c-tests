from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-base64Binary-minLength-4-NS"


@dataclass
class NistschemaSvIvAtomicBase64BinaryMinLength4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-base64Binary-minLength-4"
        namespace = "NISTSchema-SV-IV-atomic-base64Binary-minLength-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "min_length": 11,
        }
    )
