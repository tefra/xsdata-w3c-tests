from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-minExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedIntMinExclusive4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedInt-minExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-unsignedInt-minExclusive-4-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            min_exclusive=4242349370.0
        )
    )
