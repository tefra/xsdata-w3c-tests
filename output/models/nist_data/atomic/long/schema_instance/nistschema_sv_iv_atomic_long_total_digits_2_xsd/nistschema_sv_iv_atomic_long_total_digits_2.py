from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-long-totalDigits-2-NS"


@dataclass
class NistschemaSvIvAtomicLongTotalDigits2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-long-totalDigits-2"
        namespace = "NISTSchema-SV-IV-atomic-long-totalDigits-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            total_digits=5
        )
    )