from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-minInclusive-1-NS"


@dataclass
class NistschemaSvIvAtomicDateMinInclusive1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-minInclusive-1"
        namespace = "NISTSchema-SV-IV-atomic-date-minInclusive-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            min_inclusive="1970-01-01"
        )
    )
