from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicGYearMonthMinExclusive3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            min_exclusive="2029-04"
        )
    )