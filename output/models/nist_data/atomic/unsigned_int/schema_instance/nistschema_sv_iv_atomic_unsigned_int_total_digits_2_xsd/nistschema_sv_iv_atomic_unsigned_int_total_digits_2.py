from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-totalDigits-2-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedIntTotalDigits2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedInt-totalDigits-2"
        namespace = "NISTSchema-SV-IV-atomic-unsignedInt-totalDigits-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            total_digits=3
        )
    )
