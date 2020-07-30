from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedByte-minInclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedByteMinInclusive3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedByte-minInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-unsignedByte-minInclusive-3-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            min_inclusive=18
        )
    )
