from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-positiveInteger-minInclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicPositiveIntegerMinInclusive3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-positiveInteger-minInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-positiveInteger-minInclusive-3-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            min_inclusive=8.2875884136987e+17
        )
    )
