from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gMonth-minExclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicGMonthMinExclusive1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gMonth-minExclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-gMonth-minExclusive-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            min_exclusive="--01"
        )
    )