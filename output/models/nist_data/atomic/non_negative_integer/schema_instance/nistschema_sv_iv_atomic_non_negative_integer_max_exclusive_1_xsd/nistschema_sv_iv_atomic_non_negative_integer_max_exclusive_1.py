from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonNegativeInteger-maxExclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicNonNegativeIntegerMaxExclusive1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonNegativeInteger-maxExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-nonNegativeInteger-maxExclusive-1-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            max_exclusive=1.0
        )
    )