from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-maxInclusive-4-NS"


@dataclass
class NistschemaSvIvAtomicGYearMonthMaxInclusive4:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-maxInclusive-4"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-maxInclusive-4-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": "2014-07",
        }
    )
