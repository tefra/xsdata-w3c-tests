from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-positiveInteger-minExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicPositiveIntegerMinExclusive2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-positiveInteger-minExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-positiveInteger-minExclusive-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            min_exclusive=2.626388914465322e+17
        )
    )