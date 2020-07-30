from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYear-maxInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicGYearMaxInclusive4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYear-maxInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-gYear-maxInclusive-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            max_inclusive="1998"
        )
    )
