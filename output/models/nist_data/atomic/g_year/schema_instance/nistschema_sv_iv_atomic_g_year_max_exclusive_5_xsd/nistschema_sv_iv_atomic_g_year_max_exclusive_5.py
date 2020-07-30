from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYear-maxExclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicGYearMaxExclusive5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYear-maxExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-gYear-maxExclusive-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            max_exclusive="2030"
        )
    )
