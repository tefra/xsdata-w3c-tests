from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-base64Binary-length-3-NS"


@dataclass
class NistschemaSvIvAtomicBase64BinaryLength3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-base64Binary-length-3"
        namespace = "NISTSchema-SV-IV-atomic-base64Binary-length-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            length=31
        )
    )