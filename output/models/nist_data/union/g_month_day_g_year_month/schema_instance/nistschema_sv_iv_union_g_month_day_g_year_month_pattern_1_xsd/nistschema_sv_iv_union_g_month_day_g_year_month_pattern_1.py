from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-pattern-1-NS"


@dataclass
class NistschemaSvIvUnionGMonthDayGYearMonthPattern1:
    """
    :ivar value:
    """
    class Meta:
        name = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-pattern-1"
        namespace = "NISTSchema-SV-IV-union-gMonthDay-gYearMonth-pattern-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"--\d7-2\d",
        }
    )
