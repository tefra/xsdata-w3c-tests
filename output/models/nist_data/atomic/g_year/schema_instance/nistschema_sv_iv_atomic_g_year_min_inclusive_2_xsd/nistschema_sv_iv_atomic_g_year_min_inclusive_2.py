from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYear-minInclusive-2-NS"


@dataclass
class NistschemaSvIvAtomicGYearMinInclusive2:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYear-minInclusive-2"
        namespace = "NISTSchema-SV-IV-atomic-gYear-minInclusive-2-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            min_inclusive=2010.0
        )
    )