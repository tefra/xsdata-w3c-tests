from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedLong-maxExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedLongMaxExclusive2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedLong-maxExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-unsignedLong-maxExclusive-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            max_exclusive=6.211444382599346e+17
        )
    )