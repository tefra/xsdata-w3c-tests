from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-minInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedIntMinInclusive4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedInt-minInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-unsignedInt-minInclusive-4-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            min_inclusive=2912115668
        )
    )
