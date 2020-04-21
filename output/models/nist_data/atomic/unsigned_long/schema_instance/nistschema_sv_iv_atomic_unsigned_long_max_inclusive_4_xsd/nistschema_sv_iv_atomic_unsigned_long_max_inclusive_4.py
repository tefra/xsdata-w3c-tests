from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedLong-maxInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedLongMaxInclusive4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedLong-maxInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-unsignedLong-maxInclusive-4-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            max_inclusive=5.0138861320379405e+17
        )
    )
