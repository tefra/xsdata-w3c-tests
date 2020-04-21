from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-pattern-5-NS"


@dataclass
class NistschemaSvIvAtomicGYearMonthPattern5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-pattern-5"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-pattern-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            pattern=r"18\d\d-\d2"
        )
    )
