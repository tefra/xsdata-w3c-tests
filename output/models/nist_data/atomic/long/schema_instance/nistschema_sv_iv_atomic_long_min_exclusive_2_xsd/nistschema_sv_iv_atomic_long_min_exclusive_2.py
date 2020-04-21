from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-long-minExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicLongMinExclusive2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-long-minExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-long-minExclusive-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            min_exclusive=9.684029955425018e+17
        )
    )
