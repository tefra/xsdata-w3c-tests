from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-minInclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedIntMinInclusive3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedInt-minInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-unsignedInt-minInclusive-3-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            min_inclusive=2401546713.0
        )
    )
