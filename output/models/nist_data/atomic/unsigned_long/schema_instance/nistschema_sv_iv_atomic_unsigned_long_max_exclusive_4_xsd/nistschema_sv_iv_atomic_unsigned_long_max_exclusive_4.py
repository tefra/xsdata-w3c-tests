from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedLong-maxExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedLongMaxExclusive4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedLong-maxExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-unsignedLong-maxExclusive-4-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            max_exclusive=1.464937343402718e+17
        )
    )