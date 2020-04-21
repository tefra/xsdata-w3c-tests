from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-integer-maxExclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicIntegerMaxExclusive5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-integer-maxExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-integer-maxExclusive-5-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            max_exclusive=1e+18
        )
    )
