from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedByte-totalDigits-3-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedByteTotalDigits3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedByte-totalDigits-3"
        namespace = "NISTSchema-SV-IV-atomic-unsignedByte-totalDigits-3-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            total_digits=3
        )
    )