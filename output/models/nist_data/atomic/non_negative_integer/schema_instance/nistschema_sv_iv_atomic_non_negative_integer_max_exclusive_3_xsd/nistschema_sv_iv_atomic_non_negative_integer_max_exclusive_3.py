from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonNegativeInteger-maxExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicNonNegativeIntegerMaxExclusive3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonNegativeInteger-maxExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-nonNegativeInteger-maxExclusive-3-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            max_exclusive=2.78524439385077e+17
        )
    )
