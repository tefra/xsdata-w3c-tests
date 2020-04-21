from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-maxInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicDateMaxInclusive4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-maxInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-date-maxInclusive-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            max_inclusive="1971-01-23"
        )
    )
