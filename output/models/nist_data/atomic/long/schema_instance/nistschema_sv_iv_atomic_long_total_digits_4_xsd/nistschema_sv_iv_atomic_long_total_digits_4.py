from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-long-totalDigits-4-NS"


@dataclass
class NistschemaSvIvAtomicLongTotalDigits4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-long-totalDigits-4"
        namespace = "NISTSchema-SV-IV-atomic-long-totalDigits-4-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            total_digits=13
        )
    )
