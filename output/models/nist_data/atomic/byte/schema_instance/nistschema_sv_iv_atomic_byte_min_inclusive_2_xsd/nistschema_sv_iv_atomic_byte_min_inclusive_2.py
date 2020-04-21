from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-byte-minInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicByteMinInclusive2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-byte-minInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-byte-minInclusive-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            min_inclusive=35.0
        )
    )
