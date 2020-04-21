from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYear-minExclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicGYearMinExclusive4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYear-minExclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-gYear-minExclusive-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            min_exclusive=2012.0
        )
    )
