from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYear-minExclusive-3-NS"


@dataclass
class NistschemaSvIvAtomicGYearMinExclusive3:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYear-minExclusive-3"
        namespace = "NISTSchema-SV-IV-atomic-gYear-minExclusive-3-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            min_exclusive=2025.0
        )
    )
