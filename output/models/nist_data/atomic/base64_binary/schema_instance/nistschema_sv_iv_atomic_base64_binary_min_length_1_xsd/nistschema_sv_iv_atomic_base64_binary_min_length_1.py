from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-base64Binary-minLength-1-NS"


@dataclass
class NistschemaSvIvAtomicBase64BinaryMinLength1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-base64Binary-minLength-1"
        namespace = "NISTSchema-SV-IV-atomic-base64Binary-minLength-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "min_length": 1,
        }
    )
