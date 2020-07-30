from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-nonNegativeInteger-minExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicNonNegativeIntegerMinExclusive2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-nonNegativeInteger-minExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-nonNegativeInteger-minExclusive-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            min_exclusive=279497457259986536
        )
    )
