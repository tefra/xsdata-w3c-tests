from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedByte-totalDigits-1-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedByteTotalDigits1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedByte-totalDigits-1"
        namespace = "NISTSchema-SV-IV-atomic-unsignedByte-totalDigits-1-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            total_digits=1
        )
    )
