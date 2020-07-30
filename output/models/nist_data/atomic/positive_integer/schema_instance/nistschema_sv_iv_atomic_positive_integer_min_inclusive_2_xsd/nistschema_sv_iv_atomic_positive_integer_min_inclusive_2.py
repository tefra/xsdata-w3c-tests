from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-positiveInteger-minInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicPositiveIntegerMinInclusive2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-positiveInteger-minInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-positiveInteger-minInclusive-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            min_inclusive=15066261577183049
        )
    )
