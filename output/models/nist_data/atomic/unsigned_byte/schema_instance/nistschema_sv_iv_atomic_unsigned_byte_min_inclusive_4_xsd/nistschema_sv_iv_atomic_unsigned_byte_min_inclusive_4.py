from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedByte-minInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedByteMinInclusive4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedByte-minInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-unsignedByte-minInclusive-4-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            min_inclusive=25.0
        )
    )