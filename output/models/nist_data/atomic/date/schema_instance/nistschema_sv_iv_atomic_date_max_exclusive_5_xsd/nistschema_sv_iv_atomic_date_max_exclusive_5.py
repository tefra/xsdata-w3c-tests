from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-date-maxExclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicDateMaxExclusive5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-date-maxExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-date-maxExclusive-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            max_exclusive="2030-12-31"
        )
    )