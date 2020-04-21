from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonNegativeInteger-maxInclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicNonNegativeIntegerMaxInclusive3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonNegativeInteger-maxInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-nonNegativeInteger-maxInclusive-3-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            max_inclusive=1.5417363903803648e+17
        )
    )
