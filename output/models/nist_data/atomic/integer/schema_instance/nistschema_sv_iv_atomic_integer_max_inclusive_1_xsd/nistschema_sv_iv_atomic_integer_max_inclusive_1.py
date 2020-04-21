from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-integer-maxInclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicIntegerMaxInclusive1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-integer-maxInclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-integer-maxInclusive-1-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            max_inclusive=-1e+18
        )
    )
