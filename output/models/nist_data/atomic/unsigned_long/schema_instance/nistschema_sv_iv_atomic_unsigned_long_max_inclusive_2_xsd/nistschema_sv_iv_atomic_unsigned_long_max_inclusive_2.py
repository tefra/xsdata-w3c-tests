from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedLong-maxInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedLongMaxInclusive2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedLong-maxInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-unsignedLong-maxInclusive-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            max_inclusive=1.8320697001049024e+17
        )
    )