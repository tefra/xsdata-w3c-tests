from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonNegativeInteger-minInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicNonNegativeIntegerMinInclusive2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonNegativeInteger-minInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-nonNegativeInteger-minInclusive-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            min_inclusive=4.144104754943714e+17
        )
    )