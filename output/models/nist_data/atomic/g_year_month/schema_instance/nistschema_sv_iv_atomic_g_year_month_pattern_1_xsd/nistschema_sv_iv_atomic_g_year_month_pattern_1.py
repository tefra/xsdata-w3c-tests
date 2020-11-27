from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-pattern-1-NS"


@dataclass
class NistschemaSvIvAtomicGYearMonthPattern1:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-pattern-1"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-pattern-1-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "pattern": r"17\d\d-\d1",
        }
    )
