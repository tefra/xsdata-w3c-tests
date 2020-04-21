from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-minExclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedIntMinExclusive1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedInt-minExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-unsignedInt-minExclusive-1-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            min_exclusive=0.0
        )
    )
