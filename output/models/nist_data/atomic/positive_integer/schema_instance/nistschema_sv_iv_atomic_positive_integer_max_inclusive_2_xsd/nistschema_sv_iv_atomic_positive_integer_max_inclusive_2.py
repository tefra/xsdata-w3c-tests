from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-positiveInteger-maxInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicPositiveIntegerMaxInclusive2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-positiveInteger-maxInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-positiveInteger-maxInclusive-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            max_inclusive=4.232859040076749e+17
        )
    )
