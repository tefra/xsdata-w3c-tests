from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-5-NS"


@dataclass
class NistschemaSvIvAtomicGYearMonthMinExclusive5:
    class Meta:
        name = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-5"
        namespace = "NISTSchema-SV-IV-atomic-gYearMonth-minExclusive-5-NS"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
            "min_exclusive": "2030-11",
        }
    )
