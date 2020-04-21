from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYear-minInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicGYearMinInclusive4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYear-minInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-gYear-minInclusive-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            min_inclusive=1997.0
        )
    )
