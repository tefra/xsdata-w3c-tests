from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-minInclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicGYearMonthMinInclusive5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-minInclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-minInclusive-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            min_inclusive="2030-12"
        )
    )