from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-hexBinary-length-1-NS"


@dataclass
class NistschemaSvIvAtomicHexBinaryLength1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-hexBinary-length-1"
        namespace = "NISTSchema-SV-IV-atomic-hexBinary-length-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            length=1
        )
    )
