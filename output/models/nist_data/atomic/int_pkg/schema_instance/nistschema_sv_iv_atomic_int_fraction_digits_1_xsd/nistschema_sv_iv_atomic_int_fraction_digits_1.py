from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-int-fractionDigits-1-NS"


@dataclass
class NistschemaSvIvAtomicIntFractionDigits1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-int-fractionDigits-1"
        namespace = "NISTSchema-SV-IV-atomic-int-fractionDigits-1-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            fraction_digits=0
        )
    )