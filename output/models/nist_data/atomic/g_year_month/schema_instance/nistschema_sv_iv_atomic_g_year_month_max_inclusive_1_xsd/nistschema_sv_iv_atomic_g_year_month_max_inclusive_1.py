from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-maxInclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicGYearMonthMaxInclusive1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-maxInclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-maxInclusive-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            max_inclusive="1970-01"
        )
    )
