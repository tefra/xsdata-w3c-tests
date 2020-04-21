from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonNegativeInteger-maxInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicNonNegativeIntegerMaxInclusive2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonNegativeInteger-maxInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-nonNegativeInteger-maxInclusive-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            max_inclusive=4.952293111963648e+17
        )
    )
