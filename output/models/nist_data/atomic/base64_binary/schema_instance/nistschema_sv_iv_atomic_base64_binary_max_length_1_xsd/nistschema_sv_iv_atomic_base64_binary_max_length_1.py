from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-base64Binary-maxLength-1-NS"


@dataclass
class NistschemaSvIvAtomicBase64BinaryMaxLength1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-base64Binary-maxLength-1"
        namespace = "NISTSchema-SV-IV-atomic-base64Binary-maxLength-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            max_length=1
        )
    )
