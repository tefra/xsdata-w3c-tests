from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-base64Binary-maxLength-2-NS"


@dataclass
class NistschemaSvIvAtomicBase64BinaryMaxLength2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-base64Binary-maxLength-2"
        namespace = "NISTSchema-SV-IV-atomic-base64Binary-maxLength-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "max_length": 45,
        }
    )
