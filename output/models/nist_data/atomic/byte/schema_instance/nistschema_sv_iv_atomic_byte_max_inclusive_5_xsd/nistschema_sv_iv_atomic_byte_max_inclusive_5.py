from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-byte-maxInclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicByteMaxInclusive5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-byte-maxInclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-byte-maxInclusive-5-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            max_inclusive=127.0
        )
    )
