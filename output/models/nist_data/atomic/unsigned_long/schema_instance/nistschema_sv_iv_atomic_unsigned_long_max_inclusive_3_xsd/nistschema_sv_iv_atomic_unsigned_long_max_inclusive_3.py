from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedLong-maxInclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedLongMaxInclusive3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedLong-maxInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-unsignedLong-maxInclusive-3-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            max_inclusive=1.2606067654322539e+17
        )
    )
