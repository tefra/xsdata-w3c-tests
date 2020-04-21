from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-int-minExclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicIntMinExclusive2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-int-minExclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-int-minExclusive-2-NS"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True,
            min_exclusive=-1627498592.0
        )
    )
