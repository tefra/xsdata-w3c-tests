from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gDay-minExclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicGDayMinExclusive5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gDay-minExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-gDay-minExclusive-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            min_exclusive="---30"
        )
    )