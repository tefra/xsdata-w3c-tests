from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-pattern-4-NS"


@dataclass
class NistschemaSvIvAtomicGYearMonthPattern4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-pattern-4"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-pattern-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            pattern=r"17\d\d-0\d"
        )
    )