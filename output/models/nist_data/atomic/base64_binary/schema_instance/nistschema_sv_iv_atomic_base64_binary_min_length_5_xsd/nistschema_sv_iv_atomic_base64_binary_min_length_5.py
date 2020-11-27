from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-base64Binary-minLength-5-NS"


@dataclass
class NistschemaSvIvAtomicBase64BinaryMinLength5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-base64Binary-minLength-5"
        namespace = "NISTSchema-SV-IV-atomic-base64Binary-minLength-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "min_length": 74,
        }
    )
