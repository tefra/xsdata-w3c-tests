from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-integer-minExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicIntegerMinExclusive3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-integer-minExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-integer-minExclusive-3-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            min_exclusive=3.895788091075705e+17
        )
    )
