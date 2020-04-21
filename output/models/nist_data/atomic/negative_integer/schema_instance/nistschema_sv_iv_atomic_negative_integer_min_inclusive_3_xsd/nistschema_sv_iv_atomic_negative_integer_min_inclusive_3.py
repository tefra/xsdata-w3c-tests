from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-negativeInteger-minInclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicNegativeIntegerMinInclusive3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-negativeInteger-minInclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-negativeInteger-minInclusive-3-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            min_inclusive=-5.3994562298470285e+17
        )
    )
