from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-minInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedIntMinInclusive2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedInt-minInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-unsignedInt-minInclusive-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            min_inclusive=3433747195.0
        )
    )