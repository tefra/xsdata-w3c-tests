from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-integer-maxInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicIntegerMaxInclusive2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-integer-maxInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-integer-maxInclusive-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            max_inclusive=8.280084062811693e+17
        )
    )
