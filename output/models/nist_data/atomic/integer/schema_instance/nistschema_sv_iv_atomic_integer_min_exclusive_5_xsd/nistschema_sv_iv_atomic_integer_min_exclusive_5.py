from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-integer-minExclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicIntegerMinExclusive5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-integer-minExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-integer-minExclusive-5-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            min_exclusive=1e+18
        )
    )