from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-positiveInteger-minExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicPositiveIntegerMinExclusive4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-positiveInteger-minExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-positiveInteger-minExclusive-4-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            min_exclusive=5.065587274137112e+17
        )
    )