from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-unsignedInt-maxInclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicUnsignedIntMaxInclusive3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-unsignedInt-maxInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-unsignedInt-maxInclusive-3-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            max_inclusive=637454996.0
        )
    )