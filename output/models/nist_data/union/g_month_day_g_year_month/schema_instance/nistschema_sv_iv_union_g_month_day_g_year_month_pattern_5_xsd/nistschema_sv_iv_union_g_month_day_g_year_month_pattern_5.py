from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-pattern-5-NS"


@dataclass
class NistschemaSvIvUnionGMonthDayGYearMonthPattern5:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-pattern-5"
        namespace = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-pattern-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            pattern=r"19\d\d-\d9"
        )
    )