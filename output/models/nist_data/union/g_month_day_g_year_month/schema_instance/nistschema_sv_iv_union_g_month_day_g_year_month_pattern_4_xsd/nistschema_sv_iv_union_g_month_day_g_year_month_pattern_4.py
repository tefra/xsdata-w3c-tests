from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-pattern-4-NS"


@dataclass
class NistschemaSvIvUnionGMonthDayGYearMonthPattern4:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-pattern-4"
        namespace = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-pattern-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            pattern=r"18\d\d-\d0"
        )
    )
