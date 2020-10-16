from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-base64Binary-minLength-2-NS"


@dataclass
class NistschemaSvIvAtomicBase64BinaryMinLength2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-base64Binary-minLength-2"
        namespace = "NISTSchema-SV-IV-atomic-base64Binary-minLength-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "min_length": 27,
        }
    )
