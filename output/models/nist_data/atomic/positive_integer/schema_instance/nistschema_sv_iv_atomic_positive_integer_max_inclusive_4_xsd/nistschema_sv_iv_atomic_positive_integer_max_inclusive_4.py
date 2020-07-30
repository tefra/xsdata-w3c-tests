from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-positiveInteger-maxInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicPositiveIntegerMaxInclusive4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-positiveInteger-maxInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-positiveInteger-maxInclusive-4-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            max_inclusive=619618676703699189
        )
    )
